from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TwitchClips:
    def __init__(self, category: str = None, language: str = "en"):
        self.driver = webdriver.Firefox()
        self.category = category
        self.language = language
        self.driver.get("https://www.twitch.tv/directory")

