function objById( id ) {
  if (document.getElementById)
	   var returnVar = document.getElementById(id);
  else if (document.all)
	   var returnVar = document.all[id];
  else if (document.layers)
	   var returnVar = document.layers[id];
  return returnVar;
}


function newAjax() {

	var xmlHttp;

	try {
		xmlHttp = new XMLHttpRequest();
	} catch (e) {
		try {
			xmlHttp = new ActiveXObject("Msxml2.XMLHTTP");
		} catch (e) {
			try {
				xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
			} catch (e) {
				return null;
			}
		}
	}

	return xmlHttp;
}

function setCookie(c_name,value,expiredays) {
	var exdate=new Date();
	exdate.setDate(exdate.getDate()+expiredays);
	document.cookie=c_name+ "=" +escape(value)+((expiredays==null) ? "" : ";expires="+exdate.toGMTString())+";path=/;domain=.superjoesoftware.com;";
}

function getCookie(c_name) {
	if (document.cookie.length>0) {
		c_start=document.cookie.indexOf(c_name + "=");
		if (c_start!=-1) {
			c_start=c_start + c_name.length+1;
			c_end=document.cookie.indexOf(";",c_start);
			if (c_end==-1)
				c_end=document.cookie.length;
			return unescape(document.cookie.substring(c_start,c_end));
		}
	}
	return "";
}
