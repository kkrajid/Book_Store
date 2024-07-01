from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListCreateAPIView.as_view()),
    path('books/<slug:myname>/', views.BookDetailAPIView.as_view()),
    path('books/<int:pk>/comments/', views.CommentCreateAPIView.as_view()),
    path('comments/<int:pk>/', views.CommentListCreateAPIView.as_view()),
]