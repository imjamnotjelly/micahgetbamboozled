let username
let password
let headless
let login_type

function print_inputs() {
	username = document.getElementById("u_input").value
	password = document.getElementById("p_input").value
	headless = document.getElementById("headless_cb").checked
	login_type = sessionStorage.getItem("login_type")
	console.log(`Email: ${username}`)
	console.log(`Password: ${"*".repeat(password.length)}`)
	console.log(`Headless-mode: ${headless}`)
	console.log(`Platform: ${login_type}`)
}

eel.expose(return_inputs, "return_inputs")
function return_inputs() {
	return [username, password, headless, login_type]
}

eel.expose(close_window, "close_window")
function close_window() {
	window.close()
}