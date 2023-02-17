import os
import eel
from selenium import webdriver
from time import sleep
from time import strftime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

print("""               /$$                  cm   /$$                             /$$     /$$                               /$$                                     /$$                 /$$
              |__/                    | $$                            | $$    | $$                              | $$                                    | $$                | $$
 /$$$$$$/$$$$  /$$  /$$$$$$$  /$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$  | $$$$$$$   /$$$$$$  /$$$$$$/$$$$ | $$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$$$| $$  /$$$$$$   /$$$$$$$
| $$_  $$_  $$| $$ /$$_____/ |____  $$| $$__  $$ /$$__  $$ /$$__  $$|_  $$_/  | $$__  $$ |____  $$| $$_  $$_  $$| $$__  $$ /$$__  $$ /$$__  $$|____ /$$/| $$ /$$__  $$ /$$__  $$
| $$ \ $$ \ $$| $$| $$        /$$$$$$$| $$  \ $$| $$  \ $$| $$$$$$$$  | $$    | $$  \ $$  /$$$$$$$| $$ \ $$ \ $$| $$  \ $$| $$  \ $$| $$  \ $$   /$$$$/ | $$| $$$$$$$$| $$  | $$
| $$ | $$ | $$| $$| $$       /$$__  $$| $$  | $$| $$  | $$| $$_____/  | $$ /$$| $$  | $$ /$$__  $$| $$ | $$ | $$| $$  | $$| $$  | $$| $$  | $$  /$$__/  | $$| $$_____/| $$  | $$
| $$ | $$ | $$| $$|  $$$$$$$|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$  |  $$$$/| $$$$$$$/|  $$$$$$$| $$ | $$ | $$| $$$$$$$/|  $$$$$$/|  $$$$$$/ /$$$$$$$$| $$|  $$$$$$$|  $$$$$$$
|__/ |__/ |__/|__/ \_______/ \_______/|__/  |__/ \____  $$ \_______/   \___/  |_______/  \_______/|__/ |__/ |__/|_______/  \______/  \______/ |________/|__/ \_______/ \_______/
                                                 /$$  \ $$                                                                                                                      
                                                |  $$$$$$/                                                                                                                      
                                                 \______/                                                                                                                       \n""")

os.system("")
colors = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "white": "\033[39m"
}

def tprint(data, color="white"):
    print(colors[color] + f"[{strftime('%H:%M:%S')}] {data}" + "\033[0m")


def tinput(data, color="white"):
    return input(colors[color] + f"[{strftime('%H:%M:%S')}] {data}" + "\033[0m")


class untilvis:
    def __init__(self, by, content):
        self.elem = (by, content)

    def get(self):
        return wait.until(EC.visibility_of_element_located(self.elem))

    def getmulti(self):
        return wait.until(EC.presence_of_all_elements_located(self.elem))


def eleexists(id, name):
    for i in range(10):
        try:
            exists = driver.find_element(id, name)
        except NoSuchElementException:
            sleep(0.1)
        else:
            return True
    else:
        return False


tprint("Program started", "green")
eel.init("../../src")
eel.start("frontend/platform_select/platform_select.html", block=False)
tprint("Eel initialized", "green")
tprint("WARNING: DO NOT SELECT ANY GAME ELEMENTS AMID THE AUTOMATION PROCESS! THIS WILL TERMINATE THE PROGRAM!", "red")

email = ""
password = ""
headless = False
login_type = ""

while not email:
    email, password, headless, login_type = eel.return_inputs()()

eel.close_window()

tprint(f"""
Email: {email}
Password: {'*'*len(password)}
Headless: {headless}
Platform: {login_type}
""","yellow")

options = webdriver.ChromeOptions()
if headless:
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


tprint("Starting automation", "green")

wait = WebDriverWait(driver, 25)
driver.set_page_load_timeout(30)

try:

    driver.get("https://id.blooket.com/login")
    tprint("Opening login link")
    glogin = untilvis(By.CLASS_NAME, "arts__googleButton___1rop5-camelCase").get()
    glogin.click()
    sleep(2)
    cwindows = driver.window_handles
    driver.switch_to.window(cwindows[1])
    tprint("Changing window focus to popup")

    ginp = untilvis(By.ID, "identifierId").get()
    ginp.send_keys(email)
    tprint("Entering email")
    ginp.send_keys(Keys.ENTER)
    sleep(2)

    ginp = untilvis(By.CLASS_NAME, "whsOnd").get()
    tprint("Entering password")
    ginp.send_keys(password)
    ginp.send_keys(Keys.ENTER)
    tprint("Changing window focus to primary window")
    driver.switch_to.window(cwindows[0])

    sleep(15)

    for g in range(3):
        try:

            driver.get("https://play.blooket.com/solo?id=63741c005b59391c7a779d15")
            sleep(3)
            tprint("Selecting correct gamemode")
            fbutton = untilvis(By.XPATH, """//img[@alt="Factory"]""").get()
            fbutton.click()
            tprint("Inputting correct information")
            timeinput = untilvis(By.XPATH, """//input[@placeholder="Time"]""").get()
            timeinput.clear()
            timeinput.send_keys("35")

            sbutton = driver.find_element(By.CLASS_NAME, "styles__front___vcvuy-camelCase")
            sbutton.click()
            sleep(1)
            stext = untilvis(By.CLASS_NAME, "styles__button___3LSjA-camelCase").get()
            stext.click()
            sleep(1)
            tpopup = untilvis(By.CLASS_NAME, "styles__front___vcvuy-camelCase").getmulti()[1]
            tpopup.click()
            sleep(1)

            tprint(f"Started game #{g + 1}", "green")

            up_remind_amount = 0
            button = untilvis(By.CLASS_NAME, "styles__answerContainer____unYj-camelCase")
            background = untilvis(By.CLASS_NAME, "styles__feedbackContainer___2EWRn-camelCase")
            skip = untilvis(By.CLASS_NAME, "styles__skipButton___3Ppa_-camelCase")
            blook = untilvis(By.CLASS_NAME, "styles__blookChoice___1kAAj-camelCase")
            while True:
                for i in range(3):
                    tprint(f"Answering question {i + 1}/3")
                    button.get().click()
                    sleep(1.5)
                    if up_remind_amount < 3:
                        tprint("Checking for upgrade reminder")
                        if eleexists(By.CLASS_NAME, "styles__remindButton___1gTTO-camelCase"):
                            tprint("Reminder found")
                            tprint("Negating upgrade reminder")
                            reminder = driver.find_element(By.CLASS_NAME, "styles__remindButton___1gTTO-camelCase")
                            reminder.click()
                            up_remind_amount += 1
                            print(f"Eliminated reminder {up_remind_amount}/3")
                    sleep(1.5)
                    background.get().click()
                    sleep(1)
                if eleexists(By.CLASS_NAME, "styles__skipButton___3Ppa_-camelCase"):
                    tprint("Skipping upgrade")
                    skip.get().click()

                else:
                    tprint("Selecting random blook")
                    blook.get().click()

                sleep(1.5)
        except Exception:
            tprint("Game finished", "green")
            tprint("Selecting random token multiplier")
            tokenm = untilvis(By.CLASS_NAME, "styles__prizeSet___35U-m-camelCase").get()
            tokenm.click()
            sleep(10)
            continuebtn = untilvis(By.CLASS_NAME, "styles__button___22rMT-camelCase").get()
            continuebtn.click()
            tprint("Proceeding to next game")
    tprint("Automation complete", "green")
    tprint("Press enter to quit the program.", "green")
    input("")
    quit()





except Exception as error:
    tprint(f"Error: {error} ", "red")
