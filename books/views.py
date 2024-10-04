from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    permission_classes = permissions.IsAuthenticatedOrReadOnly
    authentication_classes = TokenAuthentication
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class BookDetailView(BookListView):
    lookup_field = "pk"

class BookPostView(generics.CreateAPIView):
    authentication_classes = TokenAuthentication
    permission_classes = permissions.IsAuthenticated
    serializer_class = BookSerializer
    queryset = Book.objects.all()
