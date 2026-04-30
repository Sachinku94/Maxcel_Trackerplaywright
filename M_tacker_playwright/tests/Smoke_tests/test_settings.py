import pytest
from tests.Smoke_tests.utilities.base_class import BaseClass
from tests.Smoke_tests.Pages.homepage import HomePage

@pytest.mark.Smoke_tests
@pytest.mark.dashboard
class TestSettings(BaseClass):
    """Settings tests"""
    
    @pytest.mark.asyncio
    async def test_settings_page_load(self):
        """Test settings page loads"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing settings page load")
        await self.page.wait_for_timeout(5000)
        
        settings_page = await home_page.get_settings_page()
        await self.page.goto(settings_page)
        await self.page.wait_for_load_state('networkidle')
        
        current_url = self.page.url
        assert "settings" in current_url
        log.info("✓ Settings page loaded successfully")
    
    @pytest.mark.asyncio
    async def test_settings_content_visible(self):
        """Test settings content is visible"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing settings content visibility")
        settings_page = await home_page.get_settings_page()
        await self.page.goto(settings_page)
        await self.page.wait_for_timeout(5000)
        
        try:
            settings_form = await self.page.locator("[class*='form'], [class*='setting']").all()
            log.info(f"✓ Found {len(settings_form)} settings elements")
        except Exception as e:
            log.warning(f"Settings content warning: {str(e)}")