let username
let password
let headless

function print_inputs() {
	username = document.getElementById("u_input").value
	password = document.getElementById("p_input").value
	headless = document.getElementById("headless_cb").checked
	console.log(`Username: ${username}`)
	console.log(`Password: ${password}`)
	console.log(`Headless-mode: ${headless}`)
}