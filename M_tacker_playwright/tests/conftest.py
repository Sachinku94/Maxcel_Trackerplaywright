import json
import pytest
from playwright.async_api import async_playwright
from Config.config_reader import read_config
from dotenv import load_dotenv
import os
import logging
import allure
from allure_commons.types import AttachmentType
import asyncio
import threading

load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logfile.log')]
)


@pytest.fixture(scope="function")
async def setup(request):
    """Function-scoped fixture: start Playwright, open a browser/page, and attach to the test class.

    Using function scope forces teardown after each test so browsers don't remain open.
    """
    base_url = read_config("URL", "base_url")
    log = logging.getLogger(__name__)

    p = await async_playwright().start()
    browser = await p.chromium.launch(headless=False, slow_mo=100)
    context = await browser.new_context(record_video_dir="videos/")
    page = await context.new_page()

    try:
        await page.goto(base_url)
        log.info(f"Navigated to {base_url}")

        try:
            await page.wait_for_load_state('networkidle', timeout=15000)
        except Exception:
            pass

        try:
            if os.getenv("USER_NAME"):
                await page.fill('input[name="email"]', os.getenv("USER_NAME"))
            if os.getenv("PASSWORD"):
                await page.fill('input[name="password"]', os.getenv("PASSWORD"))
            try:
                await page.click('button[type="submit"]')
                await page.wait_for_load_state('networkidle', timeout=15000)
                log.info("User logged in successfully")
            except Exception:
                log.debug("Login submit not present or login step skipped")
        except Exception as e:
            log.error(f"Login failed: {str(e)}")
            # continue; some tests may not require login

        # Attach to class so tests can use self.page
        if hasattr(request, "cls") and request.cls is not None:
            request.cls.page = page
            request.cls.context = context
            request.cls.browser = browser
            request.cls.log = log

        yield page

    finally:
        try:
            await context.close()
        except Exception:
            log.debug("context close failed or already closed")
        try:
            await browser.close()
        except Exception:
            log.debug("browser close failed or already closed")
        try:
            await p.stop()
        except Exception:
            log.debug("playwright stop failed or already stopped")
        log.info("Browser closed (fixture)")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Loop-safe hook to capture screenshot and logs on test failure.

    Schedules the async capture on the running loop if present, otherwise runs the
    capture in a background thread to avoid 'Cannot run the event loop while another loop is running'.
    """
    outcome = yield
    rep = outcome.get_result()
    log = logging.getLogger(__name__)

    is_failed = rep.failed
    page = None

    if hasattr(item, "cls") and item.cls and hasattr(item.cls, "page"):
        page = item.cls.page

    if not (is_failed and page):
        return

    async def _capture_and_attach():
        try:
            screenshot = await page.screenshot()
            allure.attach(
                screenshot,
                name=f"Screenshot_{rep.when}_{item.name}",
                attachment_type=AttachmentType.PNG
            )

            page_content = await page.content()
            allure.attach(
                page_content,
                name=f"HTML_Source_{item.name}",
                attachment_type=AttachmentType.HTML
            )
            log.info(f"[Allure] Automated captures triggered on {rep.when} phase.")
        except Exception as e:
            log.exception(f"[Allure] Failed during async capture: {e}")

    try:
        try:
            running_loop = asyncio.get_running_loop()
        except RuntimeError:
            running_loop = None

        if running_loop and running_loop.is_running():
            running_loop.call_soon_threadsafe(asyncio.create_task, _capture_and_attach())
            log.info("[Allure] Scheduled async captures on running event loop.")
        else:
            def _run_in_thread():
                try:
                    new_loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(new_loop)
                    new_loop.run_until_complete(_capture_and_attach())
                except Exception as e:
                    log.exception(f"[Allure] Background capture failed: {e}")
                finally:
                    try:
                        asyncio.set_event_loop(None)
                    except Exception:
                        pass
                    try:
                        new_loop.close()
                    except Exception:
                        pass

            t = threading.Thread(target=_run_in_thread, daemon=True)
            t.start()
            t.join(timeout=6)
    except Exception as e:
        log.error(f"[Allure] Failed to schedule/capture: {e}")