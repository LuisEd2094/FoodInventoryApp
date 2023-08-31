from django.core.management.base import BaseCommand
from house.models import Ingredients

class Command(BaseCommand):
    help = "Creates Ingredients"
    
    def handle(self, *args, **options):
        ingredients = [
            {'name' : "Potato"},
            {'name' : "Tomato"},
            {'name' : "Flour"},
        ]
        for ingredient in ingredients:
            if not Ingredients.objects.filter(name = ingredient['name']).exists():
                new = Ingredients(**ingredient)
                new.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully created ingredient: {new}'))
            else:
                self.stdout.write(self.style.NOTICE(f"Ingredient {ingredient['name']} already exists"))
