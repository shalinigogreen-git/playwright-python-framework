import pytest

@pytest.fixture
def test_data():
    return {
        "search_text": "Playwright Python"
    }

import pytest

@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "record_video_dir": "videos/",
        "record_video_size": {"width": 1280, "height": 720}
    }

import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path=f"screenshots/{item.name}.png")

import pytest

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call":
        # Access the page fixture from the test
        page = item.funcargs.get("page")
        if page:
            # Take a screenshot and embed it
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
            # This adds the screenshot to the HTML report
            extra.append(pytest_html.extras.image(screenshot_path))
            report.extra = extra

from datetime import datetime

def pytest_html_report_title(main):
    main.append("PROJECT PYTHON PLAYWRIGHT: Login Suite")

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([f"Run Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"])
    prefix.extend(["Test Objective: Verify all Login & Search scenarios for Production Readiness."])