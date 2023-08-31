from django import forms
from .models import House, Ingredients

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = {'name'}

class AddIngredientToHouseForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ['name']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget = forms.Select(choices=[(ingredient.name, ingredient.name) for ingredient in Ingredients.objects.all()])