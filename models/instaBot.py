#!/usr/bin/python3
""" insta bot """

from models import json, time, By
import os


class InstaBot:

    def login_insta_with_cookies(self):
        browser = self.browser
        browser.get('https://www.instagram.com/accounts/login/')
        # time.sleep(6)
        time.sleep(20)

        # load an cookies json from a file
        with open('/home/$USER/ziFlw/cookies/IG_cookie.json', 'r') as file:
            cookies = json.load(file)
            # Add cookies to the browser
            for cookie in cookies:
                if 'sameSite' in cookie and cookie['sameSite'] not in ["Strict", "Lax", "None"]:
                    del cookie['sameSite']
                browser.add_cookie(cookie)

        # Refresh the page to log in with cookies
        browser.refresh()
        # time.sleep(6)
        time.sleep(20)

    def unfollow_insta_bot(self):
        browser = self.browser
        browser.get('https://www.instagram.com/stiven9_o/')
        # time.sleep(6)
        time.sleep(20)

        browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[3]/div/a').click()
        # time.sleep(6)
        time.sleep(20)
        browser.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[4]/div[1]/div/div/div/div/div/div/div[3]/div/button').click()
        # time.sleep(6)
        time.sleep(20)
