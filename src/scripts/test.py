import eel

eel.init("../../src")

form_wait = True

@eel.expose
def wait_switch():
    form_wait = not form_wait

eel.start("frontend/login/login.html", block=False)
print("Eel initialized!")

username = ""
password = ""
headless = False

while form_wait:
    pass

username, password, headless = eel.return_inputs()()
eel.close_window()

print(f"""
Username: {username}
Password: {password}
Headless: {headless}
this is in python btw!!!
""")
eel.start("frontend/platform_select/platform_select.html", block=False)


