from django.urls import reverse, resolve

class TestUrls:
    
    def test_access_url(self):
        path_names = ['home_page', 'authors', 'author_create', 'articles', 'article_create', 'regions', 'region_create']
        
        path_slug_names = [
            'author_detail', 'author_update', 'author_delete',
            'article_detail', 'article_update', 'article_delete', 
            'region_detail', 'region_update', 'region_delete'
            ]
        
        for path_name in path_names:
            path_str = reverse(path_name) # reverse is the equivalent of the url in the templates
            assert resolve(path_str).view_name == path_name
        
        for path_slug_str in path_slug_names:
            path_str = reverse(path_slug_str,kwargs = {'slug':'fake'} )
            assert resolve(path_str).view_name == path_slug_str
