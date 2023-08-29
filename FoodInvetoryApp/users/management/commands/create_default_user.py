from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

User = get_user_model()
class Command(BaseCommand):
    help = "Creates default USER"
    def handle(self, *args, **options):
        username = 'test'
        password = 'password'
        email    =  'default@gmail.com'
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, password=password, email=email)
            self.stdout.write(self.style.SUCCESS('Default user created'))
        else:
            self.stdout.write(self.style.NOTICE('Default user already exists'))