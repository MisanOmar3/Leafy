from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import Chapter
from users.permissions import IsChapterOwner

class CreateChapterView(generics.CreateAPIView):
    serializer_class = ChapterSerializer
    permission_classes = [IsAuthenticated]
    queryset = Chapter.objects.all()

class UpdateChapterView(generics.UpdateAPIView):
    serializer_class = ChapterSerializer(partial = True)
    permission_classes = [IsChapterOwner]
    def get_queryset(self):
        return Chapter.objects.all().filter(book = self.request.data['book'])
class DeleteChapterView(generics.DestroyAPIView):
    serializer_class = ChapterSerializer
    permission_classes = [IsChapterOwner]
    def get_queryset(self):
        return Chapter.objects.all().filter(book = self.request.data['book'])

class ListChapterView(generics.ListAPIView):
    serializer_class = ChapterListSerializer
    permission_classes = [IsChapterOwner]
    def get_queryset(self):
        return Chapter.objects.all().filter(book = self.request.data['book'])
    
class RetrieveChapterView(generics.RetrieveAPIView):
    serializer_class = ChapterSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Chapter.objects.all().filter(book = self.request.data['book'])
