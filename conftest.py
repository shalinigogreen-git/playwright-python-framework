import pytest
from datetime import datetime
import os

# 1. Global Browser Settings (Video Recording)
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "record_video_dir": "videos/",
        "record_video_size": {"width": 1280, "height": 720}
    }

# 2. Shared Test Data Fixture
@pytest.fixture
def test_data():
    return {
        "search_text": "Playwright Python"
    }

# 3. Unified Hook for Screenshots and HTML Report Embedding
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    # We only take screenshots when the test actually runs ("call") and FAILS
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            # Ensure the screenshots folder exists
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")
            
            # Clean filename (removing special characters from parametrization)
            clean_name = item.name.replace("[", "_").replace("]", "_").replace("-", "_")
            screenshot_path = f"screenshots/{clean_name}.png"
            
            page.screenshot(path=screenshot_path)
            
            # Embed the screenshot directly into the HTML report
            if pytest_html:
                extra.append(pytest_html.extras.image(screenshot_path))
                report.extra = extra

# 4. Branded Report Title
def pytest_html_report_title(report):
    report.title = "PROJECT PLAYWRIGHT PYTHON: Automation Suite"

# 5. Branded Report Summary with Timestamp
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([f"<h4>Run Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</h4>"])
    prefix.extend(["<p><b>Test Objective:</b> Verify Login and Search scenarios via CSV Data-Driven Testing.</p>"])


# In your conftest.py or browser launch logic
import os

# This checks if we are running on a GitHub server
is_ci = os.getenv("CI") == "true"

browser = playwright.chromium.launch(headless=is_ci)