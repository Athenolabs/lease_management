from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Lease Details",
					"description": _("Lease Management Details"),
				},
				{
					"type": "doctype",
					"name": "Lease Renewal",
					"description": _("Lease Renewal Details"),
				},
				
			]
		},
		{
			"label": _("Masters"),
			"icon": "icon-book",
			"items": [
				{
					"type": "doctype",
					"name": "Lease",
					"description": _("LeaseDetails"),
				},
				{
					"type": "doctype",
					"name": "Lessor",
					"description": _("Lessor Details"),
				},
				{
					"type": "doctype",
					"name": "Vendor",
					"description": _("Vendor Details"),
				},
			]
		},
	]
