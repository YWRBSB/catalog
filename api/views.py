from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


# view for /api/books
class BookView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"hello": "django"}, status=status.HTTP_200_OK)
    
book_view = BookView.as_view()    
    
        
