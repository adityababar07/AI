def instagram():

    import time
    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException
    from cv2 import cv2

    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 0}
    options.add_experimental_option("prefs",prefs)
    options.add_argument("--start-maximized")
    options.add_argument('headless')
    options.add_argument("user-data-dir=selenium")

    browser = webdriver.Chrome(executable_path='/media/hacker07/Hacker07/code/AI/scraping/chromedriver', options=options)
    browser.maximize_window()
    browser.get('https://www.instagram.com/direct/inbox/')

    def wait(time):
        browser.implicitly_wait(time)
    
    def sleep(sec):
        time.sleep(sec)

    wait(10)
    try:
        username = browser.find_element_by_name('username')
        username.send_keys('_t_i_n_k_e_r_b_o_y_')
        password = browser.find_element_by_name('password')
        password.send_keys('nidhi@149489')
        password.submit()
    except NoSuchElementException:
        pass

    wait(10)
    try:
        not_now = browser.find_element_by_class_name('cmbtv')
        not_now.click()
    except NoSuchElementException:
        pass

    wait(60)
    image = "/home/hacker07/Desktop/instagram.png"
    browser.save_screenshot(image)
    browser.quit()

    sleep(2)
    image = cv2.imread(image)
    cv2.waitKey(delay=5000)
    cv2.imshow("Screenshot", image)
    cv2.waitKey(delay=10000)
    cv2.destroyAllWindows()



# wait(10)
# not_now = browser.find_element_by_class_name('aOOlW')
# not_now.click()


# webbrowser.open('https://www.instagram.com/direct/inbox/')
