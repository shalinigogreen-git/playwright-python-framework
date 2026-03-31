import pytest
import logging
from playwright.sync_api import expect

# 1. Define your data
test_data = [
    ("student", "Password123", "success"),
    ("incorrectUser", "Password123", "fail"),
    ("student", "wrongPassword", "fail"),
    ("", "", "fail")
]

@pytest.mark.parametrize("user, pw, status", test_data)
def test_login_scenarios(page, user, pw, status):
    # Create a logger for this specific test
    logger = logging.getLogger(__name__)
    
    logger.info(f"--- Starting Test Scenario: User='{user}', Expected='{status}' ---")
    
    page.goto("https://practicetestautomation.com/practice-test-login/")
    logger.info("Navigated to Login Page")

    # Fill Form
    logger.info(f"Entering username: {user}")
    page.get_by_label("Username").fill(user)
    
    logger.info("Entering password")
    page.get_by_label("Password").fill(pw)
    
    logger.info("Clicking Submit button")
    page.get_by_role("button", name="Submit").click()

    # Logic: Check outcome
    if status == "success":
        logger.info("Verifying successful login redirect...")
        expect(page).to_have_url("https://practicetestautomation.com/logged-in-successfully/")
        logger.info("✅ Login Successful URL verified.")
    else:
        logger.info("Verifying error message visibility...")
        error_msg = page.locator("#error")
        expect(error_msg).to_be_visible()
        logger.warning(f"❌ Login failed as expected for user: {user}")