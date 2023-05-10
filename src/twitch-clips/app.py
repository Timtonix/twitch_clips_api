from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TwitchClips:
    def __init__(self,language: str = "en"):
        self.driver = webdriver.Firefox()
        self.language = language
        self.category = None

    @property
    def category(self):
        return self.category

    @category.setter
    def category(self, value: str):
        self.category = value.lower()

    def load_browse_page(self):
        self.driver.get("https://www.twitch.tv/directory")

    def load_category_page(self, category: str):
        category = category.lower()
        self.driver.get(f"https://www.twitch.tv/directory/game/{category}")
        if self.driver.find_element(By.XPATH, "//div[@data-a-target='core-error-message']"):
            raise ValueError(f"{category} does not exist on Twitch")