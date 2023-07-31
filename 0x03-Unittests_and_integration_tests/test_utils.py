#!/usr/bin/env python3
"""
Implimenting estAccessNestedMap.test_access_nested_map method
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestUtils(unittest.TestCase):
    """ Test cases for access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)


if __name__ == "__main__":
    unittest.main()
