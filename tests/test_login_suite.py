import pytest

# Test Case 1: Positive Scenario
import pytest

@pytest.mark.smoke  # This is your 'Tag' to do smoke testing only to save time

def test_successful_login(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    
    page.locator("#username").fill("student")
    page.locator("#password").fill("Password123")
    page.locator("#submit").click()
    
    # Assertions
    assert "logged-in-successfully" in page.url
    assert page.locator("h1").inner_text() == "Logged In Successfully"
    # Take a manual screenshot of the success page
    page.screenshot(path="screenshots/success.png")

# Test Case 2: Negative Scenario (Wrong Password)
def test_invalid_login(page):
    page.goto("https://practicetestautomation.com/practice-test-login/")
    
    page.locator("#username").fill("incorrectUser")
    page.locator("#password").fill("wrongPassword")
    page.locator("#submit").click()
    
    # Check for the error message
    error_message = page.locator("#error")
    assert error_message.is_visible()
    assert "Your username is invalid!" in error_message.inner_text()