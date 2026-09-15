from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

# view for /api/books
class BookView(APIView):
    def get(self, request, *args, **kwargs):
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = BookSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

        


# view for /api/books/<pk>
class BookDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)


book_view = BookView.as_view()
book_detail_view = BookDetailView.as_view()