from django.urls import path
from .views import *

urlpatterns = [
    path("mine/", MyBookListView.as_view()),
    path("list/", AllBookListView.as_view()),
    path("<int:pk>/detail/", BookDetailView.as_view()),
    path("create/", BookPostView.as_view()),
    path("<int:pk>/delete/", BookDeleteView.as_view()),
    path("<int:pk>/update/", BookUpdateView.as_view())
]