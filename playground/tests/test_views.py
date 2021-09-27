from django.test import RequestFactory
from django.urls import reverse

import pytest
# Create your tests here.
from playground import views, models

@pytest.mark.django_db
class TestViews:
    
    def test_home(self):
        path = reverse('home_page')
        request = RequestFactory().get(path)

        response = views.home(request)
        assert response.status_code == 200

    def test_create_article(self):
        path = reverse('article_create')
        factory = RequestFactory() 
        data = {
            'author': '0',
            'content': 'This is some text',
            'create_article': 'create',
            'region': '0',
            'title': 'This is a title'
        }
        request = factory.post(path, data,content_type='application/json')

        response = views.create_article(request)
        assert response.status_code == 200

    def test_update_article(self, database_entities):
        path = reverse('article_update', kwargs= {'slug':'this-is-a-title'})
        factory = RequestFactory() 

        data = {
            'author': '0',
            'content': 'This is some text',
            'create_article': 'create',
            'region': '0',
            'title': 'This is a title'
        }
        request = factory.post(path, data,content_type='application/json')

        response = views.update_article(request, slug = 'this-is-a-title' )
        assert response.status_code == 200

    def test_delete_article(self, database_entities):
        path = reverse('article_delete', kwargs= {'slug':'this-is-a-title'})
        factory = RequestFactory() 

        data = {
            'author': '0',
            'content': 'This is some text',
            'delete_article': 'delete',
            'region': '0',
            'title': 'This is a title'
        }
        request = factory.post(path, data)
        
        response = views.delete_article(request, slug = 'this-is-a-title')
        assert response.status_code == 302