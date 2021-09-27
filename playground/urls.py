from django.urls import path
from . import views

# url configuration
urlpatterns = [
    # path('', views.home, name = 'redirect'),
    path('home/', views.home, name = 'home_page'), 
    
    path('articles/', views.ArticleList.as_view(), name = "articles"), 

    path('articles/<str:region_country>/', views.filter_articles, name = "articles_filter"), 

    path('article/create/', views.create_article, name = "article_create"),
    path('article/<slug:slug>/', views.ArticleDetail.as_view() , name = "article_detail"),
    path('article/update/<slug:slug>/', views.update_article, name = "article_update"),
    path('article/delete/<slug:slug>/', views.delete_article, name = "article_delete"),

    path('authors/', views.AuthorList.as_view(), name = "authors"), 
    path('author/create/', views.create_author, name = "author_create"),
    path('authors/<slug:slug>/', views.AuthorDetail.as_view() , name = "author_detail"),
    path('author/update/<slug:slug>/', views.update_author, name = "author_update"),
    path('author/delete/<slug:slug>/', views.delete_author, name = "author_delete"),

    path('regions/', views.RegionList.as_view(), name = "regions"), 
    path('region/create/', views.create_region, name = "region_create"),
    path('regions/<slug:slug>/', views.RegionDetail.as_view() , name = "region_detail"),
    path('region/update/<slug:slug>/', views.update_region, name = "region_update"),
    path('region/delete/<slug:slug>/', views.delete_region, name = "region_delete"),
]
