from django.core.management.base import BaseCommand

from djangoblog.utils import save_user_avatar
from oauth.models import OAuthUser


class Command(BaseCommand):
    help = 'sync user avatar'

    def handle(self, *args, **options):
        users = OAuthUser.objects.filter(picture__isnull=False).exclude(
            picture__istartswith='https://resource.lylinux.net').all()
        self.stdout.write('начать синхронизацию{count}аватары'.format(count=len(users)))
        for u in users:
            self.stdout.write('начать синхронизацию:{id}'.format(id=u.nikename))
            url = u.picture
            url = save_user_avatar(url)
            if url:
                self.stdout.write(
                    'завершить синхронизацию:{id}.url:{url}'.format(
                        id=u.nikename, url=url))
                u.picture = url
                u.save()
        self.stdout.write('завершить синхронизацию')
