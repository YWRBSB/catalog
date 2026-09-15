
from rest_framework.test import APITestCase
from django.urls import reverse

from api.models import Book

class BookViewTest(APITestCase):
    
    def test_response_is_correct(self):
        book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            description="Test Description"
        )

        url = reverse('api:books')
        response = self.client.get(url, format='json')
        assert response.status_code == 200
        first_book = response.data[0]
        assert first_book['title'] == book.title
        assert first_book['author'] == book.author
        assert first_book['description'] == book.description


class BookDetailViewTest(APITestCase):

    def test_returns_book_by_id(self):
        book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            description="Test Description"
        )
        other_book = Book.objects.create(
            title="Other Book",
            author="Other Author",
            description="Other Description"
        )

        url = reverse('api:book-detail', kwargs={'pk': book.pk})
        response = self.client.get(url, format='json')
        assert response.status_code == 200
        assert response.data['id'] == book.pk
        assert response.data['title'] == book.title
        assert response.data['author'] == book.author
        assert response.data['description'] == book.description

    def test_returns_404_for_missing_book(self):
        url = reverse('api:book-detail', kwargs={'pk': 999})
        response = self.client.get(url, format='json')
        assert response.status_code == 404