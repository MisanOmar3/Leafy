from rest_framework import generics, status, permissions
from .models import Rating
from .serializers import RatingSerializer

class CreateRatingView(generics.CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Rating.objects.all()

class DeleteRatingView(generics.DestroyAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Rating.objects.all().filter(owner = self.request.user)