from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    # id = models.SlugField(primary_key=True,max_length=255, editable=False)
    book_name = models.CharField(max_length=255 )
    writer = models.CharField(max_length=255)
    description = models.TextField(blank=True,null=True)
    publish_date = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        """
    	Returns a string representation of the Book object.
    	
    	:return: A string representing the book.
    	:rtype: str

    	"""
        return f"{self.book_name} by {self.writer}"

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments")
    owner_of_comment = models.ForeignKey(User, on_delete=models.CASCADE,related_name="comments")
    comment = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns a string representation of the Comment object.

        :return: A string representing the comment.
        :rtype: str
        """
        return self.comment
