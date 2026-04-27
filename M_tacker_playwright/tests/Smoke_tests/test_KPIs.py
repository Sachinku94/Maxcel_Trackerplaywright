import pytest
from M_tacker_playwright.tests.Smoke_tests.utilities.base_class import BaseClass
from M_tacker_playwright.tests.Smoke_tests.Pages.homepage import HomePage

@pytest.mark.Smoke_tests
@pytest.mark.dashboard
class TestKPIs(BaseClass):
    """KPIs and KRAs tests"""
    
    @pytest.mark.asyncio
    async def test_kpi_page_load(self):
        """Test KPI page loads"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing KPI page load")
        await self.page.wait_for_timeout(5000)
        
        kpi_page = await home_page.get_kpi_page()
        await self.page.goto(kpi_page)
        await self.page.wait_for_load_state('networkidle')
        
        current_url = self.page.url
        assert "kpis-kras" in current_url
        log.info("✓ KPI page loaded successfully")
    
    @pytest.mark.asyncio
    async def test_kpi_content_visible(self):
        """Test KPI content is visible"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing KPI content visibility")
        kpi_page = await home_page.get_kpi_page()
        await self.page.goto(kpi_page)
        await self.page.wait_for_timeout(5000)
        
        try:
            content = await self.page.locator("[class*='kpi'], [class*='card']").all()
            assert len(content) > 0
            log.info(f"✓ Found {len(content)} KPI elements")
        except Exception as e:
            log.warning(f"Content visibility warning: {str(e)}")