function move(cur, top) {

	current = parseFloat(cur);
	if(current < top){
		current *= 1.1;
		scrollTo(0, current);
		setTimeout("move('" + current + "','" + top + "')", 1);
	}

}

function scroll(locale){
	elem = document.getElementById(locale);
	move(1,elem.offsetTop);
}

function contact(){
	elem = document.getElementById("contact");
	move(1,elem.offsetTop);
}


function profile(){
	elem = document.getElementById("profile");
	move(1,elem.offsetTop)
}