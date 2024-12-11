from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from .models import Book
from .serializers import *
from users.permissions import *

class MyBookListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookListSerializer
    def get_queryset(self):
        return Book.objects.all().filter(author = self.request.user)
    
class AllBookListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BookListSerializer
    queryset = Book.objects.all()

class BookDetailView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAuthenticated]
    queryset = Book.objects.all()
    def get(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

class BookPostView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BookCreateSerializer
    queryset = Book.objects.all()
    # def create(self, request, *args, **kwargs):
    #     request.data['author'] = self.request.user.id
    #     return super().create(request, *args, **kwargs)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) 
        serializer.save(author = self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookUpdateView(generics.UpdateAPIView):
    permission_classes = [IsBookOwner]
    serializer_class = BookSerializer(partial = True)
    def get_queryset(self):
        return Book.objects.all().filter(author = self.request.user)

class BookDeleteView(generics.DestroyAPIView):
    permission_classes = [IsBookOwner]
    serializer_class = BookSerializer
    def get_queryset(self):
        return Book.objects.all().filter(author = self.request.user)