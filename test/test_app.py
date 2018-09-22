import unittest

from django_http2_push.app import PushHttp2Config


class TestAppClass(unittest.TestCase):
    def test_app_create(self):
        self.assertEqual(PushHttp2Config.name, "django_http2_push")


if __name__ == "__main__":
    unittest.main()
