from .models import *
from rest_framework.serializers import ModelSerializer

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"