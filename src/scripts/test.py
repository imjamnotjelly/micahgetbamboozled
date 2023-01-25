import eel

eel.init("../../src")
eel.start("frontend/login/login.html", block=False)
print("Eel initialized!")

username = ""
password = ""
headless = False

while not username:
    username, password, headless = eel.return_inputs()()
eel.close_window()

print(f"""
Email: {username}
Password: {"*"*len(password)}
Headless: {headless}
this is in python btw!!!
""")