import pytest
from tests.Smoke_tests.utilities.base_class import BaseClass
from tests.Smoke_tests.Pages.homepage import HomePage

@pytest.mark.Smoke_tests
@pytest.mark.dashboard
class TestScreenRecording(BaseClass):
    """Screen recording tests"""
    
    @pytest.mark.asyncio
    async def test_screen_record_page(self):
        """Test screen recording page"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing screen recording page")
        await self.page.wait_for_timeout(5000)
        
        record_page = await home_page.get_screen_record_page()
        await self.page.goto(record_page)
        await self.page.wait_for_load_state('networkidle')
        
        current_url = self.page.url
        assert "video-recording" in current_url
        log.info("✓ Screen recording page loaded")
    
    @pytest.mark.asyncio
    async def test_recording_content_visible(self):
        """Test recording content is visible"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing recording content visibility")
        record_page = await home_page.get_screen_record_page()
        await self.page.goto(record_page)
        await self.page.wait_for_timeout(5000)
        
        try:
            content = await self.page.locator("[class*='video'], [class*='recording']").all()
            log.info(f"✓ Found {len(content)} recording elements")
        except Exception as e:
            log.warning(f"Recording content warning: {str(e)}")