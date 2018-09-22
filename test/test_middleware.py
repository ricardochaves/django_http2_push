import unittest
from unittest.mock import MagicMock, patch

from django_http2_push.middleware import PushHttp2Middleware
from django_http2_push.middleware import _build_header, get_link_header_from_response


class TestPushHttp2Middleware(unittest.TestCase):
    def test__build_header(self):

        result = _build_header(["/js/main.js", "base.css"])

        self.assertEqual(result, "</js/main.js>; rel=preload, <base.css>; rel=preload")

    @patch("django_http2_push.middleware.get_link_header_from_response")
    def test_process_response_no_push_list(self, mock_get_link):
        request = {}
        response = MagicMock()

        result = PushHttp2Middleware.process_response(request, response)

        self.assertFalse(mock_get_link.called)
        self.assertEqual(result, response)

    @patch("django_http2_push.middleware._build_header")
    @patch("django_http2_push.middleware.get_link_header_from_response")
    def test_process_response_links(self, mock_get_link, mock_build):
        request = MagicMock()
        request.push_list.return_value = ["base.css"]

        response = {}

        mock_get_link.return_value = "test/link"
        mock_build.return_value = "LINK test/link"

        PushHttp2Middleware.process_response(request, response)

        mock_get_link.assert_called_once_with(response)
        mock_build.assert_called_once_with(request.push_list)
        self.assertEqual(response["Link"], "test/linkLINK test/link")

    def test_get_link_header_from_response_no_link(self):

        response = {}
        result = get_link_header_from_response(response)
        self.assertEqual(result, "")

    def test_get_link_header_from_response_with_link(self):

        response = {"Link": "base.css"}
        result = get_link_header_from_response(response)
        self.assertEqual(result, "base.css, ")


if __name__ == "__main__":
    unittest.main()
