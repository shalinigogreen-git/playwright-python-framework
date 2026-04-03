import pytest
import pandas as pd
import os
from playwright.sync_api import expect
from pages.google_page import GooglePage  # Importing your POM class

def get_search_data():
    """Helper to fetch data from CSV for Playwright Python framework"""
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "..", "search_data.csv")
    df = pd.read_csv(file_path)
    return list(df.itertuples(index=False, name=None))


@pytest.mark.parametrize("term, expected", get_search_data()) # <-- DO NOT FORGET THIS
def test_google_search_pom_ddt(page, term, expected):
    google = GooglePage(page)
    google.open()

   


    # 3. Perform the search
    google.search(str(term))

    # 4. THE FIX: Wait for the results container to actually appear
    # We use a broad locator that covers the main content area
    results_container = page.locator("#main")
    
    # 5. Professional Validation
    # We add a 10-second timeout specifically for this assertion 
    # to account for slow network rendering on Google.
    expect(results_container).to_contain_text(
        str(expected), 
        ignore_case=True, 
        timeout=10000
    )