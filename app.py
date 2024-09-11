#!/usr/bin/python3
""" main app """
from models import Banner, webdriver, BotPoints
from selenium.webdriver.firefox.options import Options
from models import PrinteDiscord
import os

if __name__ == "__main__":
    Banner().display_info()
    # options = Options()
    # options.add_argument("--headless")
    # browser = webdriver.Firefox(options=options)
    browser = webdriver.Firefox()
    bot = BotPoints(browser, username_like4like=os.environ['LIKE4LIKE_USERNAME'], password_like4like=os.environ['LIKE4LIKE_PASSWORD'])
    bot.login_like4like()
    # @llllllllllllllllogin
    try:
        bot.login_twitter_with_cookies()
    except Exception:
        PrinteDiscord('```diff\n- twiter login ❌ \n```')
        exit()
    PrinteDiscord('```diff\n+ twiter login ✅ \n```')
    try:
        bot.login_insta_with_cookies()
    except Exception:
        PrinteDiscord('```diff\n- instagram login ❌ \n```')
        exit()
    PrinteDiscord('```diff\n+ instagram login ✅ \n```')
    try:
        bot.login_face_with_cookies()
    except Exception:
        PrinteDiscord('```diff\n- facebook login ❌ \n```')
        exit()
    PrinteDiscord('```diff\n+ facebook login ✅ \n```')
    # @llllllllllllllllogin
    while True:
        bot.earnPoints_Twiter_Like()
        # bot.service_run()  # ? wait 120 minutes
