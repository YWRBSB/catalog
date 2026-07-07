from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book

# view for /api/books


class BookView(APIView):
    """ List all books, or create a new book """
    
    def get(self, request, *args, **kwargs):
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        serializer = BookSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        #print(serializer.data)
        serializer.save()
        return Response(serializer.data, status=201)

book_view = BookView.as_view()    
    
        
