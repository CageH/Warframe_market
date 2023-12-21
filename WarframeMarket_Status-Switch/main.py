import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()

#options.add_argument('--headless')

browser = webdriver.Chrome(options=options)


class online_in_game():
        try:
                browser.set_window_size(1200,1080)
                browser.get(url="https://warframe.market/uk/auth/signin")
                print("On website")
                email_input = browser.find_element(By.ID, "LoginEmail").send_keys("shadow.naight@gmail.com")
                print("Send email! :)")
                password_input = browser.find_element(By.ID, "LoginPassword")
                password_input.send_keys("6u7UvI1yUl")
                print("Send password! :)")
                time.sleep(2)
                password_input.send_keys(Keys.ENTER)
                print("Button is pressed")
                time.sleep(2)

                menu_list = browser.find_element(By.CLASS_NAME, "hamburger-button--AWabH")
                menu_list.click()
                print("Open menu")
                time.sleep(2)

                profile_container = browser.find_element(By.CLASS_NAME, "profile-container")
                profile_container.click()
                print("Show status list")
                time.sleep(2)

                online = browser.find_element(By.CLASS_NAME, "s-online") #Online
                online.click()
                time.sleep(2)
                print("Online status chenged!)")
        except Exception as ex:
                print(ex)
        finally:
                browser.close()
                browser.quit()