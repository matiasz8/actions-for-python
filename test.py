#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import TestCase, main
import main


class Test_modules(TestCase):
    def test_sum(self):
        self.assertEqual(main.sum(5, 7), 11)

    def test_phase(self):
        self.assertEqual(main.phase("a", "b"), "ab")


if __name__ == "__main__":
    main()
