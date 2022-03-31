from django.db import models
from django.contrib.auth.models import User


class ALink(models.Model):
    url = models.URLField(unique=True)

    def __str__(self):
        return self.url

    class Admin:
        pass


class Bookmark(models.Model):
    title = models.CharField(maxlength=200)
    user = models.ForeignKey(User)
    link = models.ForeignKey(ALink)

    def __str__(self):
        return '%s, %s' % (self.user.username, self.link.url)

    def get_absolute_url(self):
        return self.link.url

    class Admin:
        list_display = ('title', 'link', 'user')
        list_filter = ('user',)
        ordering = ('title',)
        search_fields = ('title',)


# START FROM PAGE #34 IF NOT WORKING... REASON FOR NOT
# WORKING IS BECAUSE OF A BUG. STUFF YOU WANT TO LINK TO 
# MUST BE ABOVE THE TABLE YOU ARE LINKING from! SQLite
# PLACES TABLES IN ALPHABETICAL ORDER BY DEFAULT.
# CAN'T BE CHANGED.


class Tag(models.Model):
    name = models.CharField(maxlength=64, unique=True)
    bookmarks = models.ManyToManyField(Bookmark)

    def __str__(self):
        return self.name

    class Admin:
        pass


# Start on 128
class SharedBookmark(models.Model):
    bookmark = models.ForeignKey(Bookmark, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=1)
    users_voted = models.ManyToManyField(User)

    def __str__(self):
        return '%s, %s' % (self.bookmark, self.votes)

    def get_absolute_url(self):
        return self.bookmark.link.url

    class Admin:
        pass
