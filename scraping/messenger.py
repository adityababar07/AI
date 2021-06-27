def messenger(engine):
    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException
    import time
    from cv2 import cv2
    
    def main(visibility):
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 0}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-extensions")
        options.add_argument(visibility)
        options.add_argument("user-data-dir=selenium")
    
        global browser
        browser = webdriver.Chrome(executable_path="/media/hacker07/Hacker07/code/AI/scraping/chromedriver", options=options)
        browser.get("https://www.messenger.com/t/106102277447234")
    
    
        wait(10)
        try:
            email = browser.find_element_by_name("email")
            email.send_keys('adityababar715@gmail.com')
            password = browser.find_element_by_name("pass")
            password.send_keys("nidhi@3.1428571429")
            box = browser.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div[1]/div/div[2]/div/div[7]/div[1]/div/div[2]/div[1]/div/form/div/div[2]/div/div/label[1]/input')
            browser.execute_script("arguments[0].click();", box)
            password.submit()
        except NoSuchElementException:
            pass

    def wait(time):
        browser.implicitly_wait(time)
    
    def sleep(sec):
        time.sleep(sec)

    main('headless')
    wait(60)
    sleep(5)
    image = "/home/hacker07/Desktop/messenger.png"
    sleep(3)
    browser.save_screenshot(image)
    browser.quit()

    sleep(2)
    image = cv2.imread(image)
    cv2.waitKey(delay=5000)
    cv2.imshow("Screenshot", image)
    cv2.waitKey(delay=10000)
    cv2.destroyAllWindows()

    choice = input("Do you want to send a message(y/n) :-\t")
    if choice == "y":
        main("--start-maximized")
        time = time.perf_counter()
        for _ in range(3):
            if time >= 300:
                choice1 = input("Do you wanna countinue ? (y/n):-\t")
                if choice1 == "y":
                    continue
                else:
                    browser.quit()
                    break
    else:
        engine("you have to make me more brilliant later")
    