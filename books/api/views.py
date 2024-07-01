from rest_framework.generics import GenericAPIView
from books.models import Book, Comment
from books.api.serializer import BookSerializer, CommentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
#Concrete views
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView,CreateAPIView
from books.api.permission import IsAdminOrStaffOrReadOnly,IsCommentOwnerOrReadOnly
SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
NOT_SAFE_METHODS = ('POST', 'PUT', 'PATCH', 'DELETE')
from rest_framework.exceptions import ValidationError


class BookListCreateAPIView(ListCreateAPIView):
    """
    A view that provides GET (list) and POST (create) operations for Book objects.
    
    Attributes:
        queryset: The queryset of Book objects available for listing.
        serializer_class: The serializer class for serializing and deserializing Book objects.
        permission_classes: The permission classes used to check user permissions.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrStaffOrReadOnly]

class BookDetailAPIView(RetrieveUpdateAPIView):
    """
    API view for retrieving and updating a single Book object.

    Attributes:
        queryset (QuerySet): All Book objects.
        serializer_class (Serializer): BookSerializer.
        lookup_field (str): The primary key of the Book object.
        lookup_url_kwarg (str): The name of the URL parameter used to identify the Book object.
        permission_classes (list): List of permission classes. Only admin users are allowed.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'myname'
    permission_classes = [permissions.IsAdminUser]
   

class CommentCreateAPIView(CreateAPIView):
    """
    A view for creating a new comment in the API.
    
    Attributes:
    - queryset: The queryset used to fetch all comments from the database.
    - serializer_class: The serializer used to serialize and deserialize the data.
    
    Methods:
    - perform_create: Saves the serialized data to the database, with the `book_id` field set to the value of `pk` from the URL kwargs.
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self,serializer):
        """ 
        Saves the serialized data to the database, with the `book_id` field set to the value of `pk` from the URL kwargs.

        :param serializer: The serializer instance containing the data to be saved.
        :type serializer: rest_framework.serializers.Serializer
        :return: None
        """
        check_comments = Comment.objects.filter(book_id=self.kwargs.get('pk'),owner_of_comment=self.request.user)
        if check_comments.exists():
            raise ValidationError("You have already commented on this book")
        book_id = self.kwargs.get('pk')
        print("self",self.request.user.id)
        serializer.save(book_id=book_id,owner_of_comment=self.request.user)

class CommentListCreateAPIView(RetrieveUpdateAPIView):
    """
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'
    permission_classes = [IsCommentOwnerOrReadOnly]

# class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'description' 
#     lookup_url_kwarg = 'myname'
    
# class BookListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
#       queryset = Book.objects.all()
#       serializer_class = BookSerializer


#       def get(self, request, *args, **kwargs):
#            return self.list(request, *args, **kwargs)


      
#       def post(self, request, *args, **kwargs):
#           return self.create(request, *args, **kwargs)