from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()

class Command(BaseCommand):
    help = "Creates default USER"
    
    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, help='Username for the new user')
        parser.add_argument('--email', type=str, help='Email for the new user')
    
    def handle(self, *args, **options):
        provided_username = options['username']
        provided_email = options['email']
        if provided_username and provided_email:
            password = 'password' 
            if not User.objects.filter(username=provided_username).exists():
                User.objects.create_user(username=provided_username, password=password, email=provided_email)
                self.stdout.write(self.style.SUCCESS(f'User {provided_username} created'))
            else:
                self.stdout.write(self.style.NOTICE(f'User {provided_username} already exists'))
        else:
            default_username = 'test'
            default_email = 'default@gmail.com'
            default_password = 'password'
            if not User.objects.filter(username=default_username).exists():
                User.objects.create_user(username=default_username, password=default_password, email=default_email)
                self.stdout.write(self.style.SUCCESS('Default user created'))
            else:
                self.stdout.write(self.style.NOTICE('Default user already exists'))
