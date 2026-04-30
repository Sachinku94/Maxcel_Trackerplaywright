import json
import pytest
from playwright.async_api import async_playwright, Page, Browser, BrowserContext
from Config.config_reader import read_config
from dotenv import load_dotenv
import os
import logging
import allure
from allure_commons.types import AttachmentType

load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('logfile.log')]
)

@pytest.fixture(scope="class")
async def setup(request):
    """Fixture to set up Playwright browser and authenticate user"""
    base_url = read_config("URL", "base_url")
    log = logging.getLogger(__name__)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=100)
        context = await browser.new_context(record_video_dir="videos/")
        page = await context.new_page()
        
        await page.goto(base_url)
        log.info(f"Navigated to {base_url}")
        
        try:
            await page.wait_for_load_state('networkidle', timeout=15000)
        except:
            pass
        
        try:
            await page.fill('input[name="email"]', os.getenv("USER_NAME"))
            await page.fill('input[name="password"]', os.getenv("PASSWORD"))
            await page.click('button[type="submit"]')
            
            await page.wait_for_load_state('networkidle', timeout=15000)
            log.info("User logged in successfully")
        except Exception as e:
            log.error(f"Login failed: {str(e)}")
            await browser.close()
            raise
        
        request.cls.page = page
        request.cls.browser = browser
        request.cls.context = context
        request.cls.log = log
        
        yield page
        
        await context.close()
        await browser.close()
        log.info("Browser closed")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture screenshot and logs on test failure"""
    outcome = yield
    rep = outcome.get_result()
    log = logging.getLogger(__name__)
    
    is_failed = rep.failed
    page = None
    
    if item.cls and hasattr(item.cls, "page"):
        page = item.cls.page
    
    if is_failed and page:
        try:
            screenshot = page.screenshot()
            allure.attach(
                screenshot,
                name=f"Screenshot_{rep.when}_{item.name}",
                attachment_type=AttachmentType.PNG
            )
            
            page_content = page.content()
            allure.attach(
                page_content,
                name=f"HTML_Source_{item.name}",
                attachment_type=AttachmentType.HTML
            )
            
            log.info(f"[Allure] Automated captures triggered on {rep.when} phase.")
        except Exception as e:
            log.error(f"[Allure] Failed to capture: {str(e)}")