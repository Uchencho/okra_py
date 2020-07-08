from unittest import TestCase

from okra_py.auth import Okra_Auth
from okra_py.errors import MissingTokenError

class OkraAuthTest(TestCase):
    def test_token_error(self):
        with self.assertRaises(MissingTokenError) as context:
            Okra_Auth()
        self.assertTrue(context.exception)