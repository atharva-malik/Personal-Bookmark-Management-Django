from django.contrib.syndication.feeds import Feed
from models import SharedBookmark
from django.utils.feedgenerator import Atom1Feed
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


class RecentBookmarks(Feed):
    title = 'Django Bookmarks | Recent Bookmarks'
    link = '/feeds/recent'
    description = 'Recent bookmarks posted to Django Bookmarks'
    feed_type = Atom1Feed

    def items(self):
        return SharedBookmark.objects.order_by('-id')[:10]


class UserBookmarks(Feed):
    def get_object(self, bits):
        if len(bits) != 1:
            raise ObjectDoesNotExist
        return User.objects.get(username=bits[0])

    def title(self, user):
        return 'Django Bookmarks | Bookmarks for %s' % user.username

    def link(self, user):
        return '/feeds/user/%s/' % user.username

    def description(self, user):
        return 'Recent bookmarks posted by %s' % user.username

    def items(self, user):
        userbookmarks = []
        for bookmark in SharedBookmark.objects.all():
            if bookmark.bookmark.user.username == user.username:
                userbookmarks.append(bookmark)

        userbookmarks = userbookmarks[:10]
        return userbookmarks
