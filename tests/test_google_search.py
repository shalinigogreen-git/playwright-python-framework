import pytest
import pandas as pd
import os
from playwright.sync_api import expect

def get_search_data():
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, "..", "search_data.csv")
    df = pd.read_csv(file_path)
    return list(df.itertuples(index=False, name=None))

@pytest.mark.parametrize("term, expected", get_search_data())
def test_google_search_ddt(page, term, expected):
    page.goto("https://www.google.com")

    # Handle the 'Accept all' button for Google
    accept_btn = page.get_by_role("button", name="Accept all")
    if accept_btn.is_visible():
        accept_btn.click()

    # Using .locator() is more stable than get_by_name in some environments
    search_bar = page.locator("input[name='q']")
    # 2. WAIT for it to be visible (This fixes the Timeout)
    search_bar.wait_for(state="visible", timeout=5000)
    search_bar.fill(str(term))
    search_bar.press("Enter")

    # Wait for results to load and check the search container
    # We use a broader locator to avoid timing issues on production sites
    expect(page.locator("body")).to_contain_text(str(expected))