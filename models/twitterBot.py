#!/usr/bin/python3
""" twitter bot """

from models import json, time, By
import os


class TwitterBot:

    def login_twitter_with_cookies(self):
        browser = self.browser
        browser.get('https://twitter.com')
        #time.sleep(6)
        time.sleep(20)

        # load an cookies json from a file
        with open('/home/$USER/ziFlw/cookies/X_cookie.json', 'r') as file:
            cookies = json.load(file)
            # Add cookies to the browser
            for cookie in cookies:
                if 'sameSite' in cookie and cookie['sameSite'] not in ["Strict", "Lax", "None"]:
                    del cookie['sameSite']
                browser.add_cookie(cookie)

        # Refresh the page to log in with cookies
        browser.refresh()
        #time.sleep(6)
        time.sleep(20)

    def unfollow_twitter_bot(self):
        browser = self.browser
        browser.get('https://x.com/lowprofiletires/following')
        #time.sleep(6)
        time.sleep(20)

        browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/button/div/div[2]/div[1]/div[2]/button/div/span/span').click()
        #time.sleep(6)
        time.sleep(20)
        browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/button[1]/div/span/span').click()
        #time.sleep(6)
        time.sleep(20)
