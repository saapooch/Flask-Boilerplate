import unittest
from tests.base import BaseTestCase


class TestLanding(BaseTestCase):

    def test_landing(self):

        with self.client:
            response = self.client.get(
                '/',
                follow_redirects=True
            )
        self.assertIn(b'Welcome to the Flask Boilerplate', response.data)
