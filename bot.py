# import required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


def Glogin(mail_address, password):
	# Login Page
	driver.get(
		'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

	# input Gmail
	driver.find_element(By.ID, "identifierId").send_keys(mail_address)
	driver.find_element(By.ID, "identifierNext").click()
	driver.implicitly_wait(10)

	# input Password
	driver.find_element(By.XPATH,
		'//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
	driver.implicitly_wait(10)
	driver.find_element(By.ID, "passwordNext").click()
	driver.implicitly_wait(10)

	# go to google home page
	driver.get('https://google.com/')
	driver.implicitly_wait(100)


def turnOffMicCam():
	# turn off Microphone
	time.sleep(2)
	driver.find_elements('class name', 'GKGgdd')[0].click()
	driver.implicitly_wait(3000)

	# turn off camera
	time.sleep(1)
	driver.find_elements('class name', 'GKGgdd')[1].click()
	driver.implicitly_wait(3000)


# Function to join the meeting
def joinNow():
	   # Wait for 2 seconds
    time.sleep(2)

    # Find all 'span' elements
    spans = driver.find_elements(By.TAG_NAME, "span")

    # Loop through the spans to find and click the "Ask to Join" button
    for span in spans:
        if span.text == "Use Companion Mode":
            parent = driver.execute_script("return arguments[0].parentNode;", span)
            parent.click()
            time.sleep(10)
            break



def AskToJoin():
	# Ask to Join meet
	time.sleep(5)
	driver.implicitly_wait(2000)
	driver.find_element(By.CSS_SELECTOR,
		'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
	# Ask to join and join now buttons have same xpaths


# assign email id and password
mail_address = 'sp@rapidinnovation.dev'
password = 'Coolman16!'

# create chrome instance
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
	"profile.default_content_setting_values.media_stream_mic": 1,
	"profile.default_content_setting_values.media_stream_camera": 1,
	"profile.default_content_setting_values.geolocation": 0,
	"profile.default_content_setting_values.notifications": 1
})
driver = webdriver.Chrome(options=opt)

# login to Google account
Glogin(mail_address, password)

# go to google meet
driver.get('https://meet.google.com/onn-nzwr-uzq')

turnOffMicCam()

# AskToJoin()
joinNow()
