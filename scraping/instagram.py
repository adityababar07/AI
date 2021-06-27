def instagram(engine):

    import time
    from selenium import webdriver
    from selenium.common.exceptions import NoSuchElementException
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
            executable_path='/media/hacker07/Hacker07/code/AI/scraping/chromedriver', options=options)
        browser.maximize_window()
        browser.get('https://www.instagram.com/direct/inbox/')

        wait(10)
        try:
            username = browser.find_element_by_name('username')
            username.send_keys('_t_i_n_k_e_r_b_o_y_')
            password = browser.find_element_by_name('password')
            password.send_keys('Nidhi@149489')
            password.submit()
        except NoSuchElementException:
            pass

        wait(10)
        try:
            not_now = browser.find_element_by_class_name('cmbtv')
            not_now.click()
        except NoSuchElementException:
            pass

        wait(10)
        try:
            not_now = browser.find_element_by_class_name('HoLwm')
            not_now.click()
        except NoSuchElementException:
            pass

        wait(2)
        try:
            retry = browser.find_element_by_class_name('JBIyP')
            retry.click()
        except NoSuchElementException:
            pass

    def wait(time):
        browser.implicitly_wait(time)

    def sleep(sec):
        time.sleep(sec)

    main('headless')
    wait(60)
    sleep(5)
    image = "/home/hacker07/Desktop/instagram.png"
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


# webbrowser.open('https://www.instagram.com/direct/inbox/')
