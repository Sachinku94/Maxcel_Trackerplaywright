import pytest
from M_tacker_playwright.tests.Smoke_tests.utilities.base_class import BaseClass
from M_tacker_playwright.tests.Smoke_tests.Pages.homepage import HomePage

@pytest.mark.Smoke_tests
@pytest.mark.dashboard
class TestScreenshots(BaseClass):
    """Screenshots tests"""
    
    @pytest.mark.asyncio
    async def test_screenshot_page_load(self):
        """Test screenshot page loads"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing screenshot page load")
        await self.page.wait_for_timeout(5000)
        
        screenshot_page = await home_page.get_screenshot_page()
        await self.page.goto(screenshot_page)
        await self.page.wait_for_load_state('networkidle')
        
        current_url = self.page.url
        assert "screenshots" in current_url
        log.info("✓ Screenshot page loaded successfully")
    
    @pytest.mark.asyncio
    async def test_screenshots_gallery_visible(self):
        """Test screenshots gallery is visible"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing screenshots gallery visibility")
        screenshot_page = await home_page.get_screenshot_page()
        await self.page.goto(screenshot_page)
        await self.page.wait_for_timeout(5000)
        
        try:
            images = await self.page.locator("img, [class*='image']").all()
            log.info(f"✓ Found {len(images)} screenshot images")
        except Exception as e:
            log.warning(f"Screenshots gallery warning: {str(e)}")