const login_options =  document.getElementsByClassName("b3")

let set_id = function() {
    sessionStorage.setItem("login_type", this.id)
    window.location.href = "../frontend/login/login.html"
}

for (let e of login_options) {
    e.addEventListener("click", set_id)
}