def youtube():
    from selenium import webdriver
    import time

    options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 0}
    options.add_experimental_option("prefs",prefs)
    options.add_argument("--start-maximized")
    options.add_argument("user-data-dir=selenium")

    browser = webdriver.Chrome(executable_path='/media/hacker07/Hacker07/code/AI/scraping/chromedriver', options=options)
    browser.get("https://www.youtube.com/")

    time = time.perf_counter()
    while True:
        if time >= 3000:
            browser.quit()
            break
