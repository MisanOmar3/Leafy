from django.urls import path
from .views import *

urlpatterns = [
    path("", ListChapterView.as_view()),
    path("create/", CreateChapterView.as_view()),
    path("<int:pk>/details/", RetrieveChapterView.as_view()),
    path("<int:pk>/delete/", DeleteChapterView.as_view()),
    path("<int:pk>/update/", UpdateChapterView.as_view())
]