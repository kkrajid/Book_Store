from rest_framework import serializers
from books.models import Book, Comment





class CommentSerializer(serializers.ModelSerializer):
    """
    A serializer class for serializing and deserializing instances of the Comment model.

    Attributes:
    - model: The model that the serializer is associated with (Comment).
    - exclude: A list of fields to exclude from the serializer (excluding the 'book' field).
    - fields: If uncommented, includes all fields from the model.
    - extra_kwargs: If uncommented, sets the 'book' field to read-only.
    """
    owner_of_comment = serializers.StringRelatedField()
    class Meta:
        model = Comment
        exclude = ['book']
        # fields = '__all__'
        # extra_kwargs = {'book': {'read_only': True}}
        


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    This serializer is used to convert instances of the Book model to and from
    native Python data types that can be rendered into JSON, XML or other
    content types.

    Attributes:
        comments (CommentSerializer): A serializer for the comments field.
            This field is serialized using the CommentSerializer.

    Methods:
        None
    """

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        """
        Metadata for the BookSerializer.
        """

        model = Book
        fields = '__all__'