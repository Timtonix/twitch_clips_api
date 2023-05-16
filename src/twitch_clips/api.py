import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *


class TwitchClips:
    def __init__(self,language: str = "en"):
        self.driver = webdriver.Chrome()
        self.language = language

    def load_browse_page(self):
        self.driver.get("https://www.twitch.tv/directory")

    def load_category(self, category: str):
        category = category.lower()
        self.driver.get(f"https://www.twitch.tv/directory/game/{category}")
        # Check if the category exists
        try:
            self.driver.find_element(By.CSS_SELECTOR, ".MGmly")
        except NoSuchElementException:
            raise NoSuchElementException(f"The category {category}, doesn't exist !")


if __name__ == "__main__":
    twitch = TwitchClips()
    twitch.load_category("dgfg")