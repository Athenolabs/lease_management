


cur_frm.add_fetch('t_name', 'terms', 'terms_and_conditions');


cur_frm.cscript.refresh = function(doc,cdt,cdn){
	//console.log("in refresh");
	var total=0.0;
	var cl=doc.tax || [ ]
	//console.log(cl);
	for(i=0;i<cl.length;i++){
		//console.log(cl[i].amount);
		total += flt(cl[i].amount,2);
	}
	doc.total_renewal_amount = total;
	//console.log(doc.total_renewal_amount);
	refresh_many(['total_renewal_amount']);

}