
from rest_framework.test import APITestCase
from django.urls import reverse
from api.models import Book

class BookViewTest(APITestCase):
    def test_response_is_correct(self):
        
        book = Book.objects.create(
            title='Test Book', 
            author='Test Author', 
            description='Test Description'
            )
        
        url = reverse('api:book-list')
        response = self.client.get(url, format='json')
        assert response.status_code == 200
        first_book = response.data[0]
        assert first_book['title'] == 'Test Book'
        assert first_book['author'] == 'Test Author'
        assert first_book['description'] == 'Test Description'  