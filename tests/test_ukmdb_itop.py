#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_ukmdb_itop
----------------------------------

Tests for `ukmdb_itop` module.
"""

from unittest import TestCase

import ukmdb_itop
from ukmdb_itop import itop


class TestUkmdb_itop(TestCase):

    @classmethod
    def setup_class(cls):
        pass

    def test_something(self):
        pass

    def test_ver(self):
        self.assertEqual(itop.get_mod_version(),
                         ukmdb_itop.__version__)

    @classmethod
    def teardown_class(cls):
        pass
