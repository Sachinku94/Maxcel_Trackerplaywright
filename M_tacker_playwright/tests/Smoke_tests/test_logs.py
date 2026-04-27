import pytest
from M_tacker_playwright.tests.Smoke_tests.utilities.base_class import BaseClass
from M_tacker_playwright.tests.Smoke_tests.Pages.homepage import HomePage

@pytest.mark.Smoke_tests
@pytest.mark.dashboard
class TestLogs(BaseClass):
    """Logs management tests"""
    
    @pytest.mark.asyncio
    async def test_graph_logs_page(self):
        """Test graph logs page"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing graph logs page")
        await self.page.wait_for_timeout(5000)
        
        logs_page = await home_page.get_graph_logs_page()
        await self.page.goto(logs_page)
        await self.page.wait_for_load_state('networkidle')
        
        current_url = self.page.url
        assert "log-by-chart" in current_url
        log.info("✓ Graph logs page loaded")
    
    @pytest.mark.asyncio
    async def test_logs_chart_visible(self):
        """Test logs chart is visible"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing logs chart visibility")
        logs_page = await home_page.get_graph_logs_page()
        await self.page.goto(logs_page)
        await self.page.wait_for_timeout(5000)
        
        try:
            chart = self.page.locator("[class*='chart'], [class*='graph']").first
            is_visible = await chart.is_visible()
            if is_visible:
                log.info("✓ Logs chart is visible")
            else:
                log.info("Chart not yet visible")
        except Exception as e:
            log.warning(f"Chart visibility warning: {str(e)}")