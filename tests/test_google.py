import pytest
import re  # 1. Add this import at the top
from playwright.sync_api import expect

@pytest.mark.parametrize("search_text", ["Playwright", "Python", "Testing"])
def test_search(page, search_text):
    page.goto("https://www.google.com")
    
    # Use the role locator we fixed earlier
    search_box = page.get_by_role("combobox", name="Search")
    search_box.fill(search_text)
    search_box.press("Enter")

    # 2. Update this line to use re.compile
    # re.IGNORECASE makes sure 'python' matches 'Python'
    expect(page).to_have_title(re.compile(search_text, re.IGNORECASE))


'''
from pages.google_page import GooglePage
def test_google_search(page):
    google = GooglePage(page)

    google.open()
    google.search("Playwright Python")

    assert "Playwright" in google.get_title()

    def test_google_search(page, test_data):
    page.goto("https://www.google.com")
    page.fill('textarea[name="q"]', test_data["search_text"])
    page.press('textarea[name="q"]', "Enter")

    assert "Playwright" in page.title() 

import pytest

@pytest.mark.parametrize("search_text", ["Playwright", "Python", "Testing"])
def test_search(page, search_text):
    page.goto("https://www.google.com")
    page.fill('textarea[name="q"]', search_text)
    page.press('textarea[name="q"]', "Enter")

    assert search_text.lower() in page.title().lower()'''