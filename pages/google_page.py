import random
import time
from pages.base_page import BasePage

class GooglePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # These are the attributes the error was complaining about!
        self.search_box = 'textarea[name="q"]'
        self.results = "h3"

    def open(self):
        """Navigates to Google and handles the Consent pop-up."""
        self.navigate("https://www.google.com")
        
        # Add a small human-like pause
        time.sleep(random.uniform(1, 2))
        
        # Handle 'Accept all' if it exists
        accept_btn = self.page.get_by_role("button", name="Accept all")
        try:
            if accept_btn.is_visible(timeout=2000):
                accept_btn.click()
        except:
            pass

    def search(self, text):
        """Performs a search by typing slowly like a human."""
        # This uses 'self.search_box' which we defined in __init__
        self.page.wait_for_selector(self.search_box)
        
        # 'type' with a delay is the best way to look like a human
        self.page.fill(self.search_box, "") # Clear first
        self.page.type(self.search_box, str(text), delay=random.randint(100, 200))
        self.page.press(self.search_box, "Enter")

    def get_title(self):
        return self.page.title()