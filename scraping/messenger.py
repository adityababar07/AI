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
        browser = webdriver.Chrome(
            executable_path="/media/hacker07/Hacker07/code/AI/scraping/chromedriver", options=options)
        browser.get("https://www.messenger.com/")

        wait(10)
        try:
            with open("/media/hacker07/Hacker07/code/AI/scraping/messenger_credentials.txt") as f:
                credentials = f.readlines()
                f.close()
            email = browser.find_element_by_name("email")
            email.clear()
            email.send_keys(credentials[0])
            sleep(3)
            password = browser.find_element_by_id("pass")
            password.send_keys(credentials[1])
            sleep(5)
            box = browser.find_element_by_id('u_0_0_4m')
            box.click()
            sleep(5)
            submit = browser.find_element_by_id("loginbutton")
            submit.click()
        except NoSuchElementException:
            pass

        sleep(10)

        try:
            submit = browser.find_element_by_id("loginbutton")
            submit.click()
        except:
            pass

    def wait(time):
        browser.implicitly_wait(time)

    def sleep(sec):
        time.sleep(sec)

    main('headless')
    # main("--start-maximized")
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
        print("you have to make me more brilliant later")
