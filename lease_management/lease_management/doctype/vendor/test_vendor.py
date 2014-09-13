# Copyright (c) 2013, Indictrans and Contributors
# See license.txt

import frappe
import unittest

test_records = frappe.get_test_records('Vendor')

class TestVendor(unittest.TestCase):
	pass
