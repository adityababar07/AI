from selenium import webdriver
import time

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 1}
options.add_experimental_option("prefs",prefs)

def wait(time):
    browser.implicitly_wait(time)

browser = webdriver.Chrome(executable_path="/media/hacker07/Hacker07/code/AI/scraping/chromedriver", options=options)
browser.get("https://messenger.com")

wait(5)
email = browser.find_element_by_name("email")
email.send_keys('adityababar715@gmail.com')
password = browser.find_element_by_name("pass")
password.send_keys("nidhi@3.1428571429")
password.submit()

time.sleep(15)
browser.quit()
