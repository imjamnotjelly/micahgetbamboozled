let username
let password
let headless
let login_type = location.search.substring(1);

function print_inputs() {
	username = document.getElementById("u_input").value
	password = document.getElementById("p_input").value
	headless = document.getElementById("headless_cb").checked
	console.log(`Email: ${username}`)
	console.log(`Password: ${"*".repeat(password.length)}`)
	console.log(`Headless: ${headless}`)
	console.log(`Platform: ${login_type}`)
}

eel.expose(return_inputs, "return_inputs")
function return_inputs() {
	return [username, password, headless, login_type]
}

console.log(login_type)