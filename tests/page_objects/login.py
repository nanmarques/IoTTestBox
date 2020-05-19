from selenium.webdriver.common.by import By


class LoginPage:
    URL = 'https://www.duckduckgo.com'

    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)
