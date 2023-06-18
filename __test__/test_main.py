import unittest

from unittest.mock import patch
from src.clients.http import HttpClient
from src.exceptions.user import UserNotFoundException
from src.main import get_user_by_email
from src.models.user import User


class TestHttpClient(unittest.TestCase):
    def setUp(self):
        self.client = HttpClient()

    @patch('src.clients.http.requests.get')
    def test_get_user_id_with_existing_user(self, mock_get):
        mock_response = [{'id': 1, 'email': 'nathan@yesenia.net'}]
        mock_get.return_value.json.return_value = mock_response

        user_id = get_user_by_email(mock_response, 'nathan@yesenia.net')['id']

        self.assertEqual(user_id, 1)

    @patch('src.clients.http.requests.get')
    def test_get_user_id_with_non_existing_user(self, mock_get):
        mock_response = [{'id': 2, 'email': 'john@doe.com'}]
        mock_get.return_value.json.return_value = mock_response

        with self.assertRaises(UserNotFoundException):
            get_user_by_email(mock_response, 'nathan@yesenia.net')

    @patch('src.clients.http.requests.get')
    def test_get_posts(self, mock_get):
        mock_response = [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}]
        mock_get.return_value.json.return_value = mock_response

        posts = self.client.get(f'/posts?userId={1}')

        self.assertEqual(posts, mock_response)

    @patch('src.clients.http.requests.get')
    def test_get_albums(self, mock_get):
        mock_response = [{'id': 1, 'title': 'Album 1'}, {'id': 2, 'title': 'Album 2'}]
        mock_get.return_value.json.return_value = mock_response

        albums = self.client.get(f'/albums?userId={1}')

        self.assertEqual(albums, mock_response)

    @patch('src.clients.http.requests.get')
    def test_get_photos(self, mock_get):
        mock_response = [{'id': 1, 'title': 'Photo 1'}, {'id': 2, 'title': 'Photo 2'}]
        mock_get.return_value.json.return_value = mock_response

        photos = self.client.get(f'/photos?userId={1}')

        self.assertEqual(photos, mock_response)

    def test_output_data_to_dict(self):
        output_data = User(
            user_id=1,
            posts=[{'id': 1, 'title': 'Post 1'}],
            albums=[{'id': 1, 'title': 'Album 1'}],
            photos=[{'id': 1, 'title': 'Photo 1'}],
        )

        expected_dict = {
            'userID': 1,
            'posts': [{'id': 1, 'title': 'Post 1'}],
            'albums': [{'id': 1, 'title': 'Album 1'}],
            'photos': [{'id': 1, 'title': 'Photo 1'}]
        }

        output_dict = output_data.to_dict()

        self.assertEqual(output_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
