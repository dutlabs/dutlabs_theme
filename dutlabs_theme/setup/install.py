import frappe

def remove_navbar_items():
	navbar_settings = frappe.get_single("Navbar Settings")

	navbar_items = ["Documentation", "User Forum", "Frappe School", "Frappe Support", "Report an Issue"]

	current_navbar_items = navbar_settings.help_dropdown

	for doc in current_navbar_items:
		if doc.item_label in navbar_items:
			doc.hidden = True

	navbar_settings.save()
	

def add_navbar_items():
	navbar_settings = frappe.get_single("Navbar Settings")

	erpnext_navbar_items = [
		{
			"item_label": "Documentation",
			"item_type": "Route",
			"route": "https://docs.dutlabs.com/",
			"is_standard": 1,
		},
	    {
		    "item_label": "Support",
		    "item_type": "Route",
		    "route": "https://helpdesk.dutlabs.com/",
		    "is_standard": 1,
	    },
	]

	current_navbar_items = navbar_settings.help_dropdown
	navbar_settings.set("help_dropdown", [])

	for item in erpnext_navbar_items:
		current_labels = [item.get("item_label") for item in current_navbar_items]
		if item.get("item_label") not in current_labels:
			navbar_settings.append("help_dropdown", item)

	for item in current_navbar_items:
		navbar_settings.append(
			"help_dropdown",
			{
				"item_label": item.item_label,
				"item_type": item.item_type,
				"route": item.route,
				"action": item.action,
				"is_standard": item.is_standard,
				"hidden": item.hidden,
			},
		)

	navbar_settings.save()
	
	
def add_app_name():
    frappe.db.set_single_value("Website Settings", "app_name", "Dut ERP")
	
def add_app_logo():
    frappe.db.set_single_value("Website Settings", "app_logo", "/assets/dutlabs_theme/images/dutlabs-logo.png")
	
def disable_onboarding():
	frappe.db.set_single_value("System Settings", "enable_onboarding", 0)

def after_install():
    remove_navbar_items()
    add_navbar_items()
    add_app_name()
    add_app_logo()
    disable_onboarding()
    frappe.db.commit()
