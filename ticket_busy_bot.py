#!/usr/bin/env python
#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import platform
import os


waitingRoom = ["busy.hkticketing.com","https://queue.hkticketing.com/hotshow.html"]
targetUrl = ""

driver = None
browser = "chrome"
if browser == "chrome":
    chrome_options = None
    chromedriver_path = os.path.dirname(os.path.realpath(__file__))+ "/chromedriver"
    if platform.system()=="windows":
        chromedriver_path = os.path.dirname(os.path.realpath(__file__))+ "/chromedriver"
    driver = webdriver.Chrome(options=chrome_options, executable_path=chromedriver_path)

# def checkbox_main(url):
#     ret = False
#     form_checkbox_list = None
#     try:
#         form_checkbox_list = driver.find_elements(By.CSS_SELECTOR, "input[type=checkbox]")
#         if not form_checkbox_list is None:
#             for form_checkbox in form_checkbox_list:
#                 if not form_checkbox.is_selected():
#                     form_checkbox.click()
#                     ret = True
#     except Exception as exc:
#         print("click checkbox fail")
#         pass

#     return ret


def main():
    driver.get(targetUrl)
    
    last_url = ""

    while True:
        time.sleep(0.25)
        url = ""
        try:
            url = driver.current_url
        except Exception as exc:
            pass

        if url is None:
            continue
        else:
            if len(url) == 0:
                continue

        if len(url) > 0 :
            if url != last_url:
                print(url)
            last_url = url

        # is_checkboxed = checkbox_main(url)  -> auto checkbox

        for error_url in thislist:
            if error_url in url:
                driver.get(targetUrl)


main()