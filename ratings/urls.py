from django.urls import path
from .views import *

urlpatterns = [
    path("create/", CreateRatingView.as_view()),
    path("<int:pk>/delete/", DeleteRatingView.as_view())
]