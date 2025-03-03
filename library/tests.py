from django.test import TestCase
from django.urls import reverse 
from django.contrib.auth.models import User
from .models import Book, Genre, Author

class LibraryTestCase(TestCase):
    def setUp(self):
        #  Create a Genre
        genre = Genre.objects.create(name="Fiction")
        
        #  Create an Author
        author = Author.objects.create(first_name="John", last_name="Doe")

        # Create Books for Pagination Test
        for i in range(10):
            book = Book.objects.create(title=f"Test Book {i}", genre=genre, published_date="2024-01-01")
            book.authors.add(author)

        # Create a Test User for Login Test
        self.user = User.objects.create_user(username="testuser12", password="testpassword12")

    def test_book_list_pagination(self):
        """Test if pagination works and books appear."""
        response = self.client.get(reverse('book_list') + '?page=1') 
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Book")  

    def test_member_login(self):
        """Test if a member can log in successfully."""
        response = self.client.post(reverse('member_login'), {'username': 'testuser12', 'password': 'testpassword12'})
        self.assertEqual(response.status_code, 302) 

