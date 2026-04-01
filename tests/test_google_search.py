import pytest
import pandas as pd
import os
from playwright.sync_api import expect
from pages.google_page import GooglePage  # Importing your POM class

def get_search_data():
    """Helper to fetch data from CSV for Shivansh Services framework"""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "..", "search_data.csv")
    df = pd.read_csv(file_path)
    return list(df.itertuples(index=False, name=None))

@pytest.mark.parametrize("term, expected", get_search_data())
def test_google_search_pom_ddt(page, term, expected):
    # 1. Initialize the Page Object
    google = GooglePage(page)

    # 2. Use POM methods for actions
    google.open()
    
    # Handle Google's Consent if it appears (Method inside your POM)
    # If you haven't moved the 'Accept all' logic to GooglePage yet, 
    # it's a great next step for total encapsulation!
    accept_btn = page.get_by_role("button", name="Accept all")
    if accept_btn.is_visible():
        accept_btn.click()

    # 3. Perform the search using the POM method
    google.search(str(term))

    # 4. Professional Validation
    # We still use 'expect' here because assertions belong in the Test layer
    expect(page.locator("body")).to_contain_text(str(expected))