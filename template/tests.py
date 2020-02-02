# coding=utf-8
from unittest import TestCase
from template.tmp_math import tsum, tdiff

class ExTestCase(TestCase):
    def test_tmp_sum(self):
        self.assertEqual(tsum(3, 2), 5)
    def test_tmp_diff(self):
        self.assertEqual(tdiff(3,2), 1)