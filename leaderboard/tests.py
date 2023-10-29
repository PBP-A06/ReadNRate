from django.test import TestCase, Client
from book.models import Book
from django.utils import timezone

class LeaderboardTest(TestCase):
    def test_leaderboard_url_is_exist(self):
        response = Client().get('/leaderboard/')
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_using_leaderboard_template(self):
        response = Client().get('/leaderboard/')
        self.assertTemplateUsed(response, 'leaderboard.html')

    def test_details_url_is_exist(self):
        response = Client().get('/leaderboard/book-id-1/')
        self.assertEqual(response.status_code, 200)

    def test_details_using_details_template(self):
        response = Client().get('/leaderboard/book-id-1/')
        self.assertTemplateUsed(response, 'details.html')

class TestModels(TestCase):
    def test_string_method(self):
        book = Book.objects.get(id=1)
        expected_string = "A Light in the Attic" # Sesuai dengan books.json
        self.assertEqual(str(book), expected_string)