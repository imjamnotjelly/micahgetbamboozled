let username
let password
let headless

function print_inputs(){
	username = document.getElementById("u_input").value
	password = document.getElementById("p_input").value
	headless = document.getElementById("headless_cb").checked
	console.log(`Username: ${username}`)
	console.log(`Password: ${password}`)
	console.log(`Headless: ${headless}`)
	eel.wait_switch()
}

eel.expose(return_inputs, "return_inputs")
function return_inputs() {
	return [username, password, headless]
}

eel.expose(close_window, "close_window")
function close_window() {
	window.close()
}