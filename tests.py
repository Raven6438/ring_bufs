import unittest
from typing import Any

import exceptions
import ring_buf


class CustomAssertions:
    def assertAllElementsIsNone(self, seq: list, msg: str = None):
        standard_msg = 'Not all elements is empty'
        for elem in seq:
            if elem is not None:
                raise AssertionError(msg or standard_msg)


class TestRingBuf(unittest.TestCase, CustomAssertions):
    def setUp(self):
        self.max_size: int = 10
        self.ring_buf = ring_buf.RingBuf(max_size=self.max_size)

    def test_init_ring_buf_is_empty(self):
        self.assertAllElementsIsNone(self.ring_buf.get_seq())

    def test_create_ring_buf_without_max_size(self):
        with self.assertRaises(TypeError):
            ring_buf.RingBuf()  # noqa

    def test_create_ring_buf_with_max_size_as_not_int(self):
        with self.assertRaises(exceptions.MaxSizeIsNotIntError):
            ring_buf.RingBuf(max_size='string')

    def test_create_ring_buf_with_max_size_as_negative_int(self):
        with self.assertRaises(exceptions.MaxSizeIsNotPositiveError):
            ring_buf.RingBuf(max_size=-1)

    def test_push_element(self):
        test_element: Any = 1
        self.ring_buf.push(test_element)

        self.assertIn(test_element, self.ring_buf.get_seq())
