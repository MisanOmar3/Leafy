from rest_framework import serializers
from .models import Book
from chapters.serializers import ChapterListSerializer
from ratings.serializers import *
from ratings.models import Rating


class BookSerializer(serializers.ModelSerializer):
    chapters = ChapterListSerializer(read_only = True, many = True)
    ratings = RatingSerializer(read_only = True, many = True)
    avg_rating = serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "description",
            "chapters",
            "ratings",
            "avg_rating"
        ]

    def get_avg_rating(self, obj):
        avg_rating = 0
        for rating in Rating.objects.all().filter(book = obj):
            avg_rating += rating.value
        return avg_rating



class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "title",
            "description"
        ]

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"