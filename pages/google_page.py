# pages/google_page.py
from pages.base_page import BasePage

class GooglePage(BasePage):
    def __init__(self, page):
        super().__init__(page) # This links to BasePage
        self.search_box = 'textarea[name="q"]'
        self.results = "h3"

    def open(self):
        self.navigate("https://www.google.com")

    def search(self, text):
        self.page.fill(self.search_box, text)
        self.page.press(self.search_box, "Enter")

    def get_title(self):
        return self.page.title()