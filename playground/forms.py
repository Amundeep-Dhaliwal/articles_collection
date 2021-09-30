from django import forms  
from django.utils.text import slugify

from .models import Article, Author, Region
from pprint import pprint

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'regions', 'content']
        widgets = {'regions': forms.widgets.CheckboxSelectMultiple()}

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'occupation', 'biography']

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = ['country', 'town']