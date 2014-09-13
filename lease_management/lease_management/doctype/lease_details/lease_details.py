# Copyright (c) 2013, Indictrans and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc


class LeaseDetails(Document):
	pass





@frappe.whitelist()
def make_lease_renewal(source_name, target_doc=None):
	# def postprocess(source, doc):
	# 	doc.material_request_type = "Purchase"

	doc = get_mapped_doc("Lease Details", source_name, {
		"Lease Details": {
			"doctype": "Lease Renewal",
			"validation": {
				"docstatus": ["=", 1]
			}
		},
		"Documentation Management": {
			"doctype": "Renewal Documentation Management",
			# "field_map": {
			# 	"parent": "sales_order_no",
			# 	"stock_uom": "uom"
			# }
		}
	}, target_doc)#, postprocess)

	return doc