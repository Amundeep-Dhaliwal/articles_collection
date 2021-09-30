import pytest
from mixer.backend.django import mixer
from playground.models import Article, Author, Region

@pytest.mark.django_db
class TestModels:

    def test_article_save(self):
        article = mixer.blend('playground.Article', title = 'convoluted title', slug = '')
        article.save()
        assert article.slug == 'convoluted-title'
        new_article = Article.objects.get(slug = 'convoluted-title')
        assert new_article.title == 'convoluted title'

    def test_author_save(self):
        author = mixer.blend('playground.Author', first_name = 'Amundeep', last_name = 'Dhaliwal', slug = '')
        author.save()
        assert author.slug == 'amundeep-dhaliwal'
    
    def test_region_save(self):
        region = mixer.blend('playground.Region', country = 'United Kingdom',town = 'London',  slug = '')
        region.save()
        assert region.slug == 'united-kingdom-london'