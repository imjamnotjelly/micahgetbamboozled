import eel

def main():
    eel.init("../../src")
    eel.start("frontend/login/login.html", block=False)
    print("Eel initialized!")

    username = ""
    password = ""
    headless = False

    while not username:
        username, password, headless = eel.return_inputs()()
    # eel.close_window()

    print(f"""
    Username: {username}
    Password: {password}
    Headless: {headless}
    this is in python btw!!!
    """)
    # eel.start("frontend/platform_select/platform_select.html", block=False)

if __name__ == "__main__":
    main()



