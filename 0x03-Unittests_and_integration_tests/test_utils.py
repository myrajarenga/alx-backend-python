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

    @staticmethod
    def _expected_exception_keyerror(nested_map, path):
        """using the try and excaption to get expected rseults"""
        try:
            access_nested_map(nested_map, path)
            return None
        except KeyError as e:
            return e

    @parameterized.expand([
        ({}, ["a"], KeyError),
        ({"a": 1}, ["a", "b"], KeyError),
    ])
    def test_access_nested_map_exception\
            (self, nested_map, path, expected_exception):
        """testing method to raise exceptio errors"""
        result = self._expected_exception_keyerror(nested_map, path)
        self.assertIsInstance(result, expected_exception)
        if expected_exception is KeyError:
            self.assertEqual\
                    (str(result), "Key not found: '{}'".format(path[-1]))


if __name__ == "__main__":
    unittest.main()
