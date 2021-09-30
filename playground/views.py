from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render # render returns HTML markup to the client

from django.http import HttpResponse
from django.views import generic
from .models import Article, Author, Region
from .forms import ArticleForm, AuthorForm, RegionForm
# Create your views here.
from django.utils.text import slugify
from django.db.models import Count

from pprint import pprint
from pycountry import countries
# a request handler, no template or HTML
# a view function is a function that takes a request and returns a response

slugs_to_country_names = {slugify(c.name):c.name for c in countries}

def home(request):
    return render(request, 'home.html', {'variable': {'a':'b'}})

def filter_articles(request, region_country):
    country_names = {slugify(country.name):country.name for country in countries}

    if region_country not in country_names: 
        print(region_country)
        return redirect('/articles')
    
    filtered_articles = Article.objects.filter(region__country = country_names[region_country] )

    return render(request, 'article/article_list.html', context = {'article_list': filtered_articles} )

def create_entity(request, model_form, redirect_location, html_location):
    form = model_form() 
    context = {'form':form}

    if request.method == 'POST': 
        form = model_form(request.POST)
        
        if form.is_valid():
            form.save() 
            return redirect(redirect_location)
        else:
            print(form.errors)
    
    return render(request, html_location, context)

def update_entity(request, model, model_form, slug, redirect_location, html_location):
    entity = model.objects.get(slug = slug)
    form = model_form(instance= entity)
    context = {'form':form}

    if request.method == 'POST':
        form = model_form(request.POST, instance=entity)

        if form.is_valid():

            form.save()
            return redirect(redirect_location)
        else:
            print(form.errors)

    return render(request, html_location, context)

def delete_entity(request, model, model_str, slug, html_indicator, redirect_location, html_location):
    entity = model.objects.get(slug = slug)
    context = {model_str:entity}
    
    if request.method == 'POST' and request.POST[html_indicator] == 'delete':

        entity.delete()

        return redirect(redirect_location)
    
    return render(request, html_location, context)

class ArticleList(generic.ListView):
    queryset = Article.objects.order_by('-created_on')
    template_name= 'article/article_list.html'
    model = Article

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset == False: 
            return redirect('/articles')
        else:
            return super().get(request, *args, **kwargs)

    def get_queryset(self):
        if self.kwargs == {}:
            return Article.objects.all()
        else:

            queried_countries = set(self.kwargs['regions'].split('&'))
            requested_countries = []
            for country in queried_countries: 
                if not country in slugs_to_country_names: 
                    return False
                else:
                    requested_countries.append(slugs_to_country_names[country])
            
            queried_number = len(requested_countries)
            
            query_set = Article.objects.annotate(num_regions = Count('regions')).filter(num_regions__gte =queried_number)
            
            for country_name in requested_countries:
                query_set = query_set.filter(regions__country = country_name)

            return query_set

class ArticleDetail(generic.DetailView):
    model = Article
    template_name = 'article/article_detail.html'

class AuthorList(generic.ListView):
    queryset = Author.objects.order_by('-joined')
    template_name = 'author/author_list.html'

class AuthorDetail(generic.DetailView):
    model = Author
    template_name = 'author/author_detail.html'

class RegionList(generic.ListView):
    queryset = Region.objects.order_by('-added')
    template_name = 'region/region_list.html'

class RegionDetail(generic.DetailView):
    model = Region 
    template_name = 'region/region_detail.html'


def create_article(request):
    return create_entity(
        request= request, 
        model_form= ArticleForm, 
        redirect_location= '/articles', 
        html_location= 'article/article_create.html'
    )

def update_article(request, slug):
    return update_entity(
        request= request, 
        model = Article,
        model_form= ArticleForm, 
        slug = slug, 
        redirect_location= '/articles', 
        html_location= 'article/article_create.html'
    )

def delete_article(request, slug):
    return delete_entity(
        request= request, 
        model= Article,
        model_str= 'article', 
        slug=slug, 
        html_indicator='delete_article', 
        redirect_location='/articles', 
        html_location='article/article_delete.html'
    )

def create_author(request):
    return create_entity(
        request= request, 
        model_form= AuthorForm, 
        redirect_location='/authors', 
        html_location= 'author/author_create.html'
    )

def update_author(request, slug):
    return update_entity(
        request= request, 
        model = Author, 
        model_form= AuthorForm, 
        slug = slug, 
        redirect_location= '/authors', 
        html_location= 'author/author_create.html'
    )

def delete_author(request, slug):
    return delete_entity(
        request= request, 
        model= Author,
        model_str= 'author', 
        slug=slug, 
        html_indicator='delete_author', 
        redirect_location='/authors', 
        html_location='author/author_delete.html'
    )

def create_region(request):
    return create_entity(
        request= request, 
        model_form= RegionForm, 
        redirect_location='/regions', 
        html_location= 'region/region_create.html'
    )

def update_region(request, slug):
    return update_entity(
        request= request, 
        model = Region, 
        model_form= RegionForm, 
        slug = slug, 
        redirect_location= '/regions', 
        html_location= 'region/region_create.html'
    )

def delete_region(request, slug):
    return delete_entity(
        request= request, 
        model= Region,
        model_str= 'region', 
        slug=slug, 
        html_indicator= 'delete_region', 
        redirect_location= '/regions', 
        html_location='region/region_delete.html'
    )