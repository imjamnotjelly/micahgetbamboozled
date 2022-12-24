from selenium import webdriver
from time import sleep
from time import strftime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

print("""               /$$                     /$$                             /$$     /$$                               /$$                                     /$$                 /$$
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

colors = {
    "red":"\033[31m",
    "green":"\033[32m",
    "yellow":"\033[33m",
    "white":"\033[39m"
}

def tprint(data, color = "white"):
    print(colors[color] + f"[{strftime('%H:%M:%S')}] {data}" + "\033[0m")

def tinput(data, color = "white"):
    return input(colors[color] + f"[{strftime('%H:%M:%S')}] {data}" + "\033[0m")

class untilvis:
    def __init__(self, by, content):
        self.elem = (by, content)

    def get(self):
        return wait.until(EC.visibility_of_element_located(self.elem))

    def getmulti(self):
        return wait.until(EC.presence_of_all_elements_located(self.elem))

def eleexists(id, name):
    try:
        exists = driver.find_element(id, name)
    except NoSuchElementException:
        return False
    else:
        return True


tprint("Program started", "green")
tprint("WARNING: DO NOT SELECT ANY GAME ELEMENTS AMID THE AUTOMATION PROCESS! THIS WILL TERMINATE THE PROGRAM!", "red")

while True:
    PATH = tinput(
        r"Enter the location of your Chrome WebDriver, or enter skip if it is already stored in your enviromental variables/system PATH: ", "yellow")
    try:
        if PATH.lower() == "skip":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Chrome(PATH)
    except Exception as error:
        tprint(f"Error: {error}", "red")
        tprint("The location of your Chrome WebDriver is incorrect or not present in your system PATH.", "red")
    else:
        break

while True:
    uemail = tinput("Enter your Google account email that corresponds to your blooket account:  ", "yellow")
    if "@" not in uemail or "." not in uemail:
        tprint("Please enter a valid email.", "red")
    else:
        break


upassword = tinput("Enter your Google account password:  ", "yellow")
gameamount = int(tinput("How many times would you like to run the gamemode?: ", "yellow"))
tprint("Starting automation", "green")

wait = WebDriverWait(driver, 25)
driver.set_page_load_timeout(30)


try:



    driver.get("https://id.blooket.com/login")
    tprint("Opening login link")
    glogin = driver.find_element(By.CLASS_NAME, "arts__googleButton___1rop5-camelCase")
    glogin.click()
    sleep(2)
    cwindows = driver.window_handles
    driver.switch_to.window(cwindows[1])
    tprint("Changing window focus to popup")


    ginp = untilvis(By.ID, "identifierId")
    ginp.get().send_keys(uemail)
    tprint("Entering email")
    ginp.get().send_keys(Keys.ENTER)
    sleep(2)

    ginp = untilvis(By.CLASS_NAME, "whsOnd")
    tprint("Entering password")
    ginp.get().send_keys(upassword)
    ginp.get().send_keys(Keys.ENTER)
    tprint("Changing window focus to primary window")
    driver.switch_to.window(cwindows[0])

    sleep(15)

    for g in range(gameamount):
        try:

            driver.get("https://play.blooket.com/solo?id=63741c005b59391c7a779d15")
            sleep(3)
            tprint("Selecting correct gamemode")
            fbutton = driver.find_element(By.XPATH, """//img[@alt="Factory"]""")
            fbutton.click()


            tprint("Inputting correct information")
            timeinput = driver.find_element(By.XPATH, """//input[@placeholder="Time"]""")
            timeinput.clear()
            timeinput.send_keys("30")

            sbutton = driver.find_element(By.CLASS_NAME, "styles__front___vcvuy-camelCase")
            sbutton.click()
            sleep(1)
            stext = driver.find_element(By.CLASS_NAME, "styles__button___3LSjA-camelCase")
            stext.click()
            sleep(1)
            tpopup = driver.find_elements(By.CLASS_NAME, "styles__front___vcvuy-camelCase")[1]
            tpopup.click()
            sleep(1)

            tprint(f"Started game #{g+1}", "green")
            while True:
                for i in range(3):
                    tprint(f"Answering question {i+1}/3")
                    button = untilvis(By.CLASS_NAME, "styles__answerContainer____unYj-camelCase")
                    button.get().click()
                    sleep(2)
                    tprint("Checking for upgrade reminder")
                    if eleexists(By.CLASS_NAME, "styles__remindButton___1gTTO-camelCase"):
                        tprint("Reminder found")
                        tprint("Negating upgrade reminder")
                        reminder = driver.find_element(By.CLASS_NAME, "styles__remindButton___1gTTO-camelCase")
                        reminder.click()
                    sleep(1.5)
                    background = untilvis(By.CLASS_NAME, "styles__feedbackContainer___2EWRn-camelCase")
                    background.get().click()
                    sleep(1)
                if eleexists(By.CLASS_NAME, "styles__skipButton___3Ppa_-camelCase"):
                    tprint("Skipping upgrade")
                    skip = driver.find_element(By.CLASS_NAME, "styles__skipButton___3Ppa_-camelCase")
                    skip.click()

                else:
                    tprint("Selecting random blook")
                    blook = untilvis(By.CLASS_NAME, "styles__blookChoice___1kAAj-camelCase")
                    blook.get().click()

                sleep(1.5)
        except:
            tprint("Game finished", "green")
            tprint("Selecting random token multiplier")
            tokenm = untilvis(By.CLASS_NAME, "styles__prizeSet___35U-m-camelCase")
            tokenm.get().click()
            continuebtn = untilvis(By.CLASS_NAME, "styles__button___22rMT-camelCase")
            continuebtn.get().click()
            tprint("Proceeding to next game")
    tprint("Automation complete", "green")
    for i in range(3, 0, -1):
        print(f"Quitting in: {i}")
        sleep(1)
    quit()





except Exception as error:
    tprint(f"Error: {error} ", "red")
