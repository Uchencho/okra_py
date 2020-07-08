from unittest import TestCase
from settings import token
from okra_py.auth import Okra_Auth
from okra_py.errors import MissingTokenError

class OkraAuthTest(TestCase):
    def test_a_token_error(self):
        with self.assertRaises(MissingTokenError) as context:
            Okra_Auth()
        self.assertTrue(context.exception)

    def test_b_valid_retreive_resp(self):
        okra_mod = Okra_Auth(token)
        self.assertEqual(okra_mod.retrieve_auth().status_code, 200)