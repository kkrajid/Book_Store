from django.test import TestCase
from rest_framework.test import APITestCase
from books.models import Book
from datetime import datetime
from django.utils import timezone


class BookTestCase(APITestCase):
    def setUp(self):
        """
        Set up the test environment by creating a Book object with the following attributes:
        
        - book_name: "Test Book"
        - writer: "Test Writer"
        - description: "Test Description"
        - publish_date: datetime(2022, 1, 1) converted to an aware datetime using timezone.make_aware()
        
        This function is called before each test method in the test class.
        """
        self.book = Book.objects.create(
            book_name="Test Book",
            writer="Test Writer",
            description="Test Description",
            publish_date=timezone.make_aware(datetime(2022, 1, 1)),
        )

    def test_book_creation(self):
        """
        Test the creation of a book object by asserting that its attributes match the expected values.

        This function is part of the BookTestCase class and is called during the test_book_creation method.

        The function performs the following assertions:
        - Asserts that the book_name attribute of the book object is equal to "Test Book".
        - Asserts that the writer attribute of the book object is equal to "Test Writer".
        - Asserts that the description attribute of the book object is equal to "Test Description".
        - Asserts that the publish_date attribute of the book object is equal to the aware datetime value created using timezone.make_aware() and datetime(2022, 1, 1).

        This function does not take any parameters and does not return any values.
        """
        self.assertEqual(self.book.book_name, "Test Book")
        self.assertEqual(self.book.writer, "Test Writer")
        self.assertEqual(self.book.description, "Test Description")
        self.assertEqual(self.book.publish_date, timezone.make_aware(datetime(2022, 1, 1)))

    def test_book_str(self):
        """
        Test the string representation of a book object by asserting that its string representation matches the expected value.

        This function is part of the BookTestCase class and is called during the test_book_str method.

        The function performs the following assertions:
        - Asserts that the string representation of the book object is equal to "Test Book by Test Writer".

        This function does not take any parameters and does not return any values.
        """
        self.assertEqual(str(self.book), "Test Book by Test Writer")    

    def test_book_list(self):
        """
        Test the retrieval of a list of books by asserting that the number of books retrieved is equal to 1.

        This function is part of the BookTestCase class and is called during the test_book_list method.

        The function performs the following assertions:
        - Asserts that the number of books retrieved is equal to 1.

        This function does not take any parameters and does not return any values.
        """
        books = Book.objects.all()
        self.assertEqual(len(books), 1)

    def test_book_update(self):
        """
        Test the updating of a book object by asserting that the description attribute is updated to "Updated Description".

        This function is part of the BookTestCase class and is called during the test_book_update method.

        The function performs the following assertions:
        - Asserts that the description attribute of the book object is equal to "Updated Description".

        This function does not take any parameters and does not return any values.
        """
        self.book.description = "Updated Description"
        self.book.save()
        self.assertEqual(self.book.description, "Updated Description")

    def test_book_delete(self):
        """
        Test the deletion of a book object by asserting that the book object is deleted.

        This function is part of the BookTestCase class and is called during the test_book_delete method.

        The function performs the following assertions:
        - Asserts that the book object is deleted.

        This function does not take any parameters and does not return any values.
        """
        self.book.delete()
        books = Book.objects.all()
        self.assertEqual(len(books), 0)


