#!/usr/bin/python3
""" earn points from like4like.org """

import time
from selenium.webdriver.common.by import By
from .twitterBot import TwitterBot
from .services import Service
from .instaBot import InstaBot
from .faceBot import FaceBot


class BotPoints(TwitterBot, Service, InstaBot, FaceBot):

    def __init__(self, browser, username_like4like, password_like4like):
        self.browser = browser
        self.username_like4like = username_like4like
        self.password_like4like = password_like4like
        self.SERVICES = [self.earnPoints_Twiter_follow, self.earnPoints_Twiter_Like,
                         self.earnPoints_Twiter_Retweet, self.earnPoints_Instagram_Like,
                         self.earnPoints_Instagram_Follow, self.earnPoints_Facebook_Like
                         ]
        self.INDX_SERVICE = 0

    def service_run(self):
        if self.INDX_SERVICE == len(self.SERVICES):
            from models.discordPrinte import PrinteDiscord
            PrinteDiscord('```CS\n\' BotPoints is slepping 5h... \'\n```')
            time.sleep(18000) # 5 hours sleeping
            self.INDX_SERVICE = 0
        self.SERVICES[self.INDX_SERVICE]()

    def login_like4like(self):
        browser = self.browser
        browser.get('https://www.like4like.org/login/')
        #time.sleep(6)
        time.sleep(20)

        username_input = browser.find_element(By.NAME, 'username')
        password_input = browser.find_element(By.NAME, 'password')

        username_input.send_keys(self.username_like4like)
        password_input.send_keys(self.password_like4like)
        browser.find_element(By.CSS_SELECTOR, 'span.button').click()

        #time.sleep(6)
        time.sleep(20)
