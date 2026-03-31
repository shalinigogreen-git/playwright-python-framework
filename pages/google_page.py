class GooglePage:

    def __init__(self, page):
        self.page = page
        self.search_box = 'textarea[name="q"]'
        self.results = "h3"

    def open(self):
        self.page.goto("https://www.google.com")

    def search(self, text):
        self.page.fill(self.search_box, text)
        self.page.press(self.search_box, "Enter")

    def get_title(self):
        return self.page.title()