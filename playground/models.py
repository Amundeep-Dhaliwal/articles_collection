from django.db import models
from pycountry import countries
from django.utils.text import slugify
# Create your models here.
# define the model classes for this app 
# model classes pull out data from the database and present it to the user

# ! on_delete signifies a special way of removing items

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    biography = models.TextField() 
    slug = models.SlugField(unique = True, null = False, blank = True)
    joined = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ['-joined']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.first_name} {self.last_name}')
        return super().save(*args, **kwargs)


class Region(models.Model):
    country_options = sorted([(country.name,country.name) for country in countries])
    country = models.CharField(max_length= 200, choices = country_options)
    town = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(unique = True, null = False, blank = True)
    # does one need a many to many relationship here

    def __str__(self):
        return f'{self.country}, {self.town}'

    class Meta:
        ordering = ['-added']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.country} {self.town}')
        return super().save(*args, **kwargs)

class Article(models.Model):
    title = models.CharField(max_length=200, unique = True)
    slug = models.SlugField(unique = True, null = False, blank = True)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on = models.DateTimeField(auto_now = True)
    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE) # exception resolved by deleting db, makemigrations and migrate
    content = models.TextField()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)