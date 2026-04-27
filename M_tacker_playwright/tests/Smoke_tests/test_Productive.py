import pytest
from M_tacker_playwright.tests.Smoke_tests.utilities.base_class import BaseClass
from M_tacker_playwright.tests.Smoke_tests.Pages.homepage import HomePage

@pytest.mark.Smoke_tests
@pytest.mark.dashboard
class TestProductivity(BaseClass):
    """Productivity metrics tests"""
    
    @pytest.mark.asyncio
    async def test_most_productive_page(self):
        """Test most productive page"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing most productive page")
        await self.page.wait_for_timeout(5000)
        
        prod_page = await home_page.get_productivity_page()
        await self.page.goto(prod_page)
        await self.page.wait_for_load_state('networkidle')
        
        current_url = self.page.url
        assert "most-productive" in current_url
        log.info("✓ Most productive page loaded")
    
    @pytest.mark.asyncio
    async def test_unproductive_page(self):
        """Test unproductive page"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing unproductive page")
        await self.page.wait_for_timeout(5000)
        
        unprod_page = await home_page.get_unproductive_page()
        await self.page.goto(unprod_page)
        await self.page.wait_for_load_state('networkidle')
        
        current_url = self.page.url
        assert "most-unproductive" in current_url
        log.info("✓ Unproductive page loaded")
    
    @pytest.mark.asyncio
    async def test_idle_page(self):
        """Test idle page"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing idle page")
        await self.page.wait_for_timeout(5000)
        
        idle_page = await home_page.get_idle_page()
        await self.page.goto(idle_page)
        await self.page.wait_for_load_state('networkidle')
        
        current_url = self.page.url
        assert "most-idle" in current_url
        log.info("✓ Idle page loaded")
    
    @pytest.mark.asyncio
    async def test_best_performer_page(self):
        """Test best performer page"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing best performer page")
        await self.page.wait_for_timeout(5000)
        
        best_page = await home_page.get_best_performer_page()
        await self.page.goto(best_page)
        await self.page.wait_for_load_state('networkidle')
        
        current_url = self.page.url
        assert "best-performance" in current_url
        log.info("✓ Best performer page loaded")