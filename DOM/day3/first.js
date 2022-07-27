// function sendData(event) {
// 	event.preventDefauly();
// 	let username = document.forms[0].elements[0].value
// 	console.log(username);
// }

// // <form onsubmit="sendData(event)" method="get" name="form1">
// //     <input type="text" name="username" value="" id="username" placeholder="username">
// //     <input type="text" name="password" value="" id="password" placeholder="password">
// //     <input type="submit" name="" value="Submit">
// // </form>

let id;
function start(){
	let box = document.getElementById('inner')
	let pos = 0;
	let id = setInterval(function() {
		if(pos == 350) {
		clearInterval(id)
	}
	else {
		pos++
		box.style.left = pos + 'px';
		box.style.top = pos + 'px';
	}
	},10)
}


