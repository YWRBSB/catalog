from django.urls import re_path
from .views import book_detail_view, book_view

app_name = "api"

urlpatterns = [
    re_path(r'^books/$', book_view, name='book-list'),
    re_path(r'^books/(?P<pk>[0-9]+)/$', book_detail_view, name='book-detail'),
    
]
