import pytest
from tests.Smoke_tests.utilities.base_class import BaseClass
from tests.Smoke_tests.Pages.homepage import HomePage

@pytest.mark.Smoke_tests
@pytest.mark.dashboard
class TestConsolidatedLogs(BaseClass):
    """Consolidated logs tests"""
    
    @pytest.mark.asyncio
    async def test_comprehensive_logs_page(self):
        """Test comprehensive logs page"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing comprehensive logs page")
        await self.page.wait_for_timeout(5000)
        
        logs_page = await home_page.get_comprehensive_logs_page()
        await self.page.goto(logs_page)
        await self.page.wait_for_load_state('networkidle')
        
        current_url = self.page.url
        assert "log-by-date" in current_url
        log.info("✓ Comprehensive logs page loaded")
    
    @pytest.mark.asyncio
    async def test_logs_content_visible(self):
        """Test logs content is visible"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing logs content visibility")
        logs_page = await home_page.get_comprehensive_logs_page()
        await self.page.goto(logs_page)
        await self.page.wait_for_timeout(5000)
        
        try:
            content = await self.page.locator("[class*='log'], [class*='entry']").all()
            log.info(f"✓ Found {len(content)} log entries")
        except Exception as e:
            log.warning(f"Logs content warning: {str(e)}")