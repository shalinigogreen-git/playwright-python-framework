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