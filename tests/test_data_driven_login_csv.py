import pytest
import pandas as pd
import logging
import re
from playwright.sync_api import expect

# 1. Professional CSV Data Loader

import os

def get_csv_data():
    # This finds the folder where THIS script is sitting
    current_dir = os.path.dirname(__file__)
    # This points to the file one level up (in the root folder)
    file_path = os.path.join(current_dir, "..", "test_data.csv")
    
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Loaded {len(df)} test cases from CSV file.")
        return list(df.itertuples(index=False, name=None))
    except Exception as e:
        # If it fails, let's print EXACTLY where it looked so we can fix it
        pytest.exit(f"❌ Looking for file at: {os.path.abspath(file_path)}\nError: {e}")


# 2. The Smart Data-Driven Test
@pytest.mark.parametrize("user, pw, status", get_csv_data())
def test_login_from_csv(page, user, pw, status):
    logging.info(f"--- Testing Login for: {user} | Expected Outcome: {status} ---")
    
    page.goto("https://practicetestautomation.com/practice-test-login/")
    
    # Fill fields (str() ensures numbers like 123 in CSV don't cause errors)
    page.get_by_label("Username").fill(str(user))
    page.get_by_label("Password").fill(str(pw))
    
    logging.info(f"Attempting login for user: {user}")
    page.get_by_role("button", name="Submit").click()

    # Logic: Validate based on CSV 'status' column
    if str(status).strip().lower() == "success":
        logging.info("Checking for successful login redirect...")
        expect(page).to_have_url(re.compile("logged-in-successfully"))
    else:
        logging.info("Checking for error message visibility...")
        error_msg = page.locator("#error")
        expect(error_msg).to_be_visible()