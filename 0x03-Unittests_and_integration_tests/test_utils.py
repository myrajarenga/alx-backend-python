#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestUtils(unittest.TestCase):
    """ Test cases for access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @staticmethod
    def _expected_exception_keyerror(nested_map, path):
        """using the try and exception to get expected results"""
        try:
            access_nested_map(nested_map, path)
            return None
        except KeyError as e:
            return e

    @parameterized.expand([
        ({}, ["a"], KeyError),
        ({"a": 1}, ["a", "b"], KeyError),
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_exception):
        result = self._expected_exception_keyerror(nested_map, path)
        self.assertIsInstance(result, expected_exception)
        if expected_exception is KeyError:
            self.assertEqual(str(result), f"Key not found: '{path[-1]}'")


class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('test_utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        """Configure the mock_requests_get
        to return a mock response
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_requests_get.return_value = mock_response

        """" Call the get_json function"""
        result = get_json(test_url)

        mock_requests_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
