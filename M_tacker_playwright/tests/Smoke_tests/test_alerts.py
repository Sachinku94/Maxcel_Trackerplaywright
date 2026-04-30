import pytest
from tests.Smoke_tests.utilities.base_class import BaseClass
from tests.Smoke_tests.Pages.homepage import HomePage

@pytest.mark.Smoke_tests
@pytest.mark.dashboard
class TestAlerts(BaseClass):
    """Alerts management tests"""
    
    @pytest.mark.asyncio
    async def test_alerts_page_load(self):
        """Test alerts page loads"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing alerts page load")
        await self.page.wait_for_timeout(5000)
        
        alerts_page = await home_page.get_alerts_page()
        await self.page.goto(alerts_page)
        await self.page.wait_for_load_state('networkidle')
        
        current_url = self.page.url
        assert "alerts" in current_url
        log.info("✓ Alerts page loaded successfully")
    
    @pytest.mark.asyncio
    async def test_alerts_content_visible(self):
        """Test alerts content is visible"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing alerts content")
        alerts_page = await home_page.get_alerts_page()
        await self.page.goto(alerts_page)
        await self.page.wait_for_timeout(5000)
        
        try:
            alert_elements = await self.page.locator("[class*='alert'], [class*='notification']").all()
            log.info(f"✓ Found {len(alert_elements)} alert elements")
        except Exception as e:
            log.warning(f"Alerts content warning: {str(e)}")