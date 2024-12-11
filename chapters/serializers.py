from rest_framework import serializers
from .models import Chapter

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = [
            "title",
            "body",
            "book"
        ]

class ChapterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = [
            "title"
        ]