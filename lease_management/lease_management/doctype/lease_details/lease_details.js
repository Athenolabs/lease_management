
//cur_frm.add_fetch('tc_name', 'terms', 'terms');


cur_frm.cscript.make_invoice = function(doc,cdt,cdn){
	if(doc.__islocal) {
		msgprint("For Making Invoice current form must be saved ")
	}
	else{
		var si = frappe.model.make_new_doc_and_get_name('Sales Invoice');
        	si = locals['Sales Invoice'][si];
        	si.selling_price_list='Standard Selling';
			loaddoc('Sales Invoice', si.name);
	}
}



cur_frm.cscript.refresh=function(doc,cdt,cdn){
  if(doc.docstatus == 1) {
      cur_frm.add_custom_button(frappe._('Make Lease Renewal'),
      cur_frm.cscript['Make Lease Renewal']);
   }

}

cur_frm.cscript['Make Lease Renewal'] = function() {

  frappe.model.open_mapped_doc({
    method: "lease_management.lease_management.doctype.lease_details.lease_details.make_lease_renewal",
    source_name: cur_frm.doc.name
  })

}


