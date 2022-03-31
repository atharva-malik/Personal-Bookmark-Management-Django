import os.path
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from bookmarks.views import *
from bookmarks.feeds import *

site_media = os.path.join(os.path.dirname(__file__), 'site_media')

# Make sure you add the feeds dict before URLPATTERNS object.
feeds = {
    'recent': RecentBookmarks,
    'user': UserBookmarks
}

# todo pip install django==1.1.3

urlpatterns = patterns('',
                       # Feeds
                       (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),

                       # OTHER
                       (r'^site_media/ (?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': site_media}),

                       # BROWSING
                       (r'^$', main_page),
                       (r'^user/(\w+)/$', user_page),
                       (r'^tag/(\w+)/$', tag_page),
                       (r'^popular/$', popular_page),
                       (r'^tag/$', tag_cloud_page),
                       (r'^search/$', search_page),
                       (r'^bookmark/(\d+)/$', bookmark_page),

                       # SESSION MANAGEMENT
                       (r'^login/$', 'django.contrib.auth.views.login'),
                       (r'^logout/$', logout_page),
                       (r'^admin/', include('django.contrib.admin.urls')),
                       (r'^register/$', register_page),
                       (r'^register/success/$', direct_to_template, {'template': 'registration/register_success.html'}),

                       # ACCOUNT MANAGEMENT
                       (r'^save/$', bookmark_save_page),
                       (r'^vote/$', bookmark_vote_page),
                       )

# Example:
# (r'^django_bookmarks/', include('django_bookmarks.foo.urls')),

# Uncomment this for admin:
# (r'^admin/', include('django.contrib.admin.urls')),
