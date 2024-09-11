#!/usr/bin/python3
""" services to earn points from like4like.org """

from models import By, time, WebDriverWait, EC
from .discordPrinte import PrinteDiscord

class Service:

    # @ Twitter SERVICES

    def earnPoints_Twiter_follow(self):
        browser = self.browser
        browser.get('https://www.like4like.org/earn-credits.php?feature=twitter')
        time.sleep(6)

        try:
            button = browser.find_element(By.CSS_SELECTOR, "a[class^='cursor earn_pages_button profile_view_img']")
            button.click()
            time.sleep(6)
        except Exception:
            PrinteDiscord("twitter : Follow Exepred ⚠️")
            self.INDX_SERVICE += 1
            return

        tabs = browser.window_handles   # ? Get list of all tabs

        browser.switch_to.window(tabs[1])   # @ Switch to second tab
        time.sleep(6)

        # ? Wait for the follow button to be clickable and click it
        try:
            follow_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.r-16y2uox:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)"))
            )
            follow_button.click()
            time.sleep(6)
            browser.close()
        except Exception:
            PrinteDiscord("twit : Follow button not found in twitter")
            browser.close()
            browser.switch_to.window(tabs[0])   # ? Switch back to first tab
            return

        browser.switch_to.window(tabs[0])   # ? Switch back to first tab
        time.sleep(6)

        try:
            browser.find_element(
                By.XPATH, '/html/body/div[6]/div/div[1]/div[2]/div[2]/div[4]/div[1]/div[2]/div[1]/div/div[1]/a').click()
            time.sleep(6)
        except Exception:
            PrinteDiscord("twit : Follow button not found")
            return

    def earnPoints_Twiter_Like(self):
        browser = self.browser
        browser.get('https://www.like4like.org/user/earn-twitter-favorites.php')
        time.sleep(6)

        try:
            button = browser.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div[2]/div[2]/div[4]/div[1]/div[2]/div[1]/div/div[3]/div/div/a")
            button.click()
            time.sleep(6)
        except Exception:
            PrinteDiscord("twitter : Like Exepred ⚠️")
            self.INDX_SERVICE += 1
            return

        tabs = browser.window_handles   # ? Get list of all tabs

        browser.switch_to.window(tabs[1])   # @ Switch to second tab
        time.sleep(6)

        # ? Wait for the like  to be clickable and click it
        xpaths = ["/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[5]/div/div/div[3]/button",
                  "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[2]/div/div/article/div/div/div[3]/div[5]/div/div/div[3]/button",
                  "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[3]/div/div/article/div/div/div[3]/div[5]/div/div/div[3]/button"
                  ]
        button = None
        for xpath in xpaths:
            try:
                button = browser.find_element(By.XPATH, xpath)
                break
            except Exception:
                continue

        if button is not None:
            button.click()
            time.sleep(6)
            browser.close()
        else:
            PrinteDiscord("twit: like button not found in twitter")
            browser.close()
            browser.switch_to.window(tabs[0])   # ? Switch back to first tab
            return

        browser.switch_to.window(tabs[0])   # ? Switch back to first tab
        time.sleep(6)

        try:
            browser.find_element(
                By.XPATH, '/html/body/div[6]/div/div[1]/div[2]/div[2]/div[4]/div[1]/div[2]/div[1]/div/div[1]/a').click()
            time.sleep(6)
        except Exception:
            PrinteDiscord("twit : like button not found")
            return

    def earnPoints_Twiter_Retweet(self):
        browser = self.browser
        browser.get('https://www.like4like.org/user/earn-twitter-retweet.php')
        time.sleep(6)

        try:
            button = browser.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div[2]/div[2]/div[4]/div[1]/div[2]/div[1]/div/div[3]/div/div/a")
            button.click()
            time.sleep(6)
        except Exception:
            PrinteDiscord("twitter : Retwet Exepred ⚠️")
            self.INDX_SERVICE += 1
            return

        tabs = browser.window_handles

        browser.switch_to.window(tabs[1])   # @ Switch to second tab
        time.sleep(6)

        # ? Wait for the like retwet to be clickable and click it
        try:
            follow_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[1]/div/div/article/div/div/div[3]/div[5]/div/div/div[2]/button"))
            )
            follow_button.click()
            time.sleep(6)
            browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div[2]/div/div[3]/div/div/div/div/div[2]/div/span").click()
            time.sleep(6)
            browser.close()
        except Exception:
            PrinteDiscord("twit : retwet button not found in twitter")
            browser.close()
            browser.switch_to.window(tabs[0])   # ? Switch back to first tab
            return

        browser.switch_to.window(tabs[0])   # ? Switch back to first tab
        time.sleep(6)

        try:
            browser.find_element(
                By.XPATH, '/html/body/div[6]/div/div[1]/div[2]/div[2]/div[4]/div[1]/div[2]/div[1]/div/div[1]/a').click()
            time.sleep(6)
        except Exception:
            PrinteDiscord("twit : retwet button not found")
            return

    # @ Instagram SERVICES

    def earnPoints_Instagram_Follow(self):
        browser = self.browser
        browser.get('https://www.like4like.org/user/earn-instagram-follow.php')
        time.sleep(6)

        try:
            button = browser.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div[2]/div[2]/div[4]/div[1]/div[2]/div[1]/div/div[3]/div/div/a")
            button.click()
            time.sleep(6)
        except Exception:
            PrinteDiscord("instagram : follow Exepred ⚠️")
            self.INDX_SERVICE += 1
            return

        tabs = browser.window_handles

        browser.switch_to.window(tabs[1])   # @ Switch to second tab
        time.sleep(6)

        # ? Wait for the like retwet to be clickable and click it
        try:
            follow_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[2]/div/div/div[2]/div/div[1]/button"))
            )
            follow_button.click()
            time.sleep(6)
            browser.close()
        except Exception:
            PrinteDiscord("inst: follow button not found in inst")
            browser.close()
            browser.switch_to.window(tabs[0])   # ? Switch back to first tab
            return

        browser.switch_to.window(tabs[0])   # ? Switch back to first tab
        time.sleep(6)

        try:
            browser.find_element(
                By.XPATH, '/html/body/div[6]/div/div[1]/div[2]/div[2]/div[4]/div[1]/div[2]/div[1]/div/div[1]/a').click()
            time.sleep(6)
        except Exception:
            PrinteDiscord("inst: like button not found")
            return

    def earnPoints_Instagram_Like(self):
        browser = self.browser
        browser.get('https://www.like4like.org/user/earn-instagram-like.php')
        time.sleep(6)

        try:
            button = browser.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div[2]/div[2]/div[4]/div[1]/div[2]/div[1]/div/div[3]/div/div/a")
            button.click()
            time.sleep(6)
        except Exception:
            PrinteDiscord("instagram : Like Exepred ⚠️")
            self.INDX_SERVICE += 1
            return

        tabs = browser.window_handles

        browser.switch_to.window(tabs[1])   # @ Switch to second tab
        time.sleep(6)

        # ? Wait for the like retwet to be clickable and click it
        try:
            follow_button = WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[3]/section[1]/div[1]/span[1]"))
            )
            follow_button.click()
            time.sleep(6)
            browser.close()
        except Exception:
            PrinteDiscord("inst: like button not found in inst")
            browser.close()
            browser.switch_to.window(tabs[0])   # ? Switch back to first tab
            return

        browser.switch_to.window(tabs[0])   # ? Switch back to first tab
        time.sleep(6)

        try:
            browser.find_element(
                By.XPATH, '/html/body/div[6]/div/div[1]/div[2]/div[2]/div[4]/div[1]/div[2]/div[1]/div/div[1]/a').click()
            time.sleep(6)
        except Exception:
            PrinteDiscord("inst: like button not found")
            return

    # @ Facebook SERVICES

    def earnPoints_Facebook_Like(self):
        browser = self.browser
        browser.get('https://www.like4like.org/user/earn-facebook.php')
        time.sleep(6)

        try:
            button = browser.find_element(By.XPATH, "/html/body/div[6]/div/div[1]/div[2]/div[2]/div[4]/div[1]/div[3]/div[1]/div/div[3]/div/div/a")
            button.click()
            time.sleep(6)
        except Exception:
            PrinteDiscord("faceboock : Like Exepred ⚠️")
            self.INDX_SERVICE += 1
            return

        tabs = browser.window_handles

        browser.switch_to.window(tabs[1])   # @ Switch to second tab
        time.sleep(6)

        # ? Wait for the like  to be clickable and click it
        xpaths = [
            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div/div[1]/div[2]/span/span",
            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[3]/div/div/div/div[1]/div[2]/span/span",
            "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[4]/div/div/div[1]/div/div[2]/div/div[1]/div[1]/div[1]/div[2]/span/span"
        ]
        button = None
        for xpath in xpaths:
            try:
                button = browser.find_element(By.XPATH, xpath)
                break
            except Exception:
                continue

        if button is not None:
            button.click()
            time.sleep(6)
            browser.close()
        else:
            PrinteDiscord("face: like button not found")
            browser.close()
            browser.switch_to.window(tabs[0])   # ? Switch back to first tab
            return

        browser.switch_to.window(tabs[0])   # ? Switch back to first tab
        time.sleep(6)

        try:
            browser.find_element(
                By.XPATH, '/html/body/div[6]/div/div[1]/div[2]/div[2]/div[4]/div[1]/div[3]/div[1]/div/div[1]/a').click()
            time.sleep(6)
        except Exception:
            PrinteDiscord("inst: like button not found")
            return
