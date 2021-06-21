def instagram():
    import time
    from selenium import webdriver

    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 1}
    options.add_experimental_option("prefs",prefs)


    browser = webdriver.Chrome(executable_path='/media/hacker07/Hacker07/code/AI/scraping/chromedriver', options=options)
    browser.get('https://www.instagram.com/direct/inbox/')

    def wait(time):
        browser.implicitly_wait(time)

    wait(10)
    username = browser.find_element_by_name('username')
    username.send_keys('_t_i_n_k_e_r_b_o_y_')
    password = browser.find_element_by_name('password')
    password.send_keys('nidhi@149489')
    password.submit()

    wait(10)
    # touch = webdriver.common.touch_actions.TouchActions
    not_now = browser.find_element_by_class_name('cmbtv')
    not_now.click()

    time.sleep(20)
    browser.quit()
# wait(10)
# not_now = browser.find_element_by_class_name('aOOlW')
# not_now.click()


# webbrowser.open('https://www.instagram.com/direct/inbox/')
