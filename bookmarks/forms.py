from django import newforms as forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    name = forms.CharField(label='First name', max_length=150)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(), max_length=32)
    password2 = forms.CharField(label='Password Again', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.clean_data:
            password1 = self.clean_data['password1']
            password2 = self.clean_data['password2']
            if password1 == password2:
                return password2
            else:
                raise forms.ValidationError('Passwords Do Not Match.')
        else:
            raise forms.ValidationError('Invalid Password.')

    def clean_username(self):
        username = self.clean_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
        try:
            User.objects.get(username=username)
            raise forms.ValidationError('That username is already taken.')
        except ObjectDoesNotExist:
            return username


class BookmarkSaveForm(forms.Form):
    url = forms.URLField(
        label='Full URL',
        widget=forms.TextInput(attrs={'size': 64})
    )
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={'size': 64})
    )
    tags = forms.CharField(
        label='Tags',
        required=False,
        widget=forms.TextInput(attrs={'size': 64}),
        help_text='Separated by a space ( ).'
    )
    share = forms.BooleanField(
        label='Share on the main page',
        required=False
    )


class SearchForm(forms.Form):
    query = forms.CharField(
        label='Enter a keyword to search for',
        widget=forms.TextInput(attrs={'size': 32})
    )
