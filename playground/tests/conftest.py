import pytest
from playground import models

@pytest.fixture
def database_entities():
    author_0 = models.Author(
                first_name = 'Algebra', 
                last_name = 'Calculus', 
                biography = 'Mathematical foundations', 
                occupation = 'Mother nature'
            )
    author_0.save() 

    region_0 = models.Region(
            country = 'United Kingdom', 
            town = 'London', 
        )
    region_0.save()

    article_0 = models.Article(
        title = 'This is a title', 
        author = author_0, 
        # regions = region_0,
        content = 'This is some text'
    )
    article_0.save() 

    return (author_0, region_0, article_0)