from django.test import TestCase

from .utils import get_username

class ApiTestCase(TestCase):
    def test_cek_username(self):
        username = get_username('tesprogrammer')
        self.assertEqual(username, 'tesprogrammer071223C10')