import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from django_http2_push.templatetags.static_push import StaticPushNode
from django_http2_push.templatetags.static_push import do_static_push


class TestStaticPush(unittest.TestCase):
    @patch.object(StaticPushNode, "handle_token", return_value=MagicMock())
    def test_do_static_push(self, mock_static):

        result = do_static_push(MagicMock(), MagicMock())

        self.assertIsInstance(result, MagicMock)

    # @patch.object(StaticNode, "render")
    # def test_render(self, mocked_super):

    #     StaticPushNode().render(None)

    #     self.assertEqual(1, 1)
