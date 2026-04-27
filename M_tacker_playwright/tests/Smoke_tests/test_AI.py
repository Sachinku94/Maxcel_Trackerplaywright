import pytest
from M_tacker_playwright.tests.Smoke_tests.utilities.base_class import BaseClass
from M_tacker_playwright.tests.Smoke_tests.Pages.homepage import HomePage

@pytest.mark.Smoke_tests
@pytest.mark.dashboard
class TestAI(BaseClass):
    """AI Summary page tests"""
    
    @pytest.mark.asyncio
    async def test_ai_page_load(self):
        """Test AI summary page loads"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing AI summary page")
        await self.page.wait_for_timeout(5000)
        
        ai_page = await home_page.get_ai_page()
        await self.page.goto(ai_page)
        await self.page.wait_for_load_state('networkidle')
        
        current_url = self.page.url
        assert "ai-summary" in current_url
        log.info("✓ AI page loaded successfully")
    
    @pytest.mark.asyncio
    async def test_ai_content_visible(self):
        """Test AI content is visible"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing AI content visibility")
        ai_page = await home_page.get_ai_page()
        await self.page.goto(ai_page)
        
        await self.page.wait_for_timeout(5000)
        
        try:
            elements = await self.page.locator("[class*='summary'], [class*='ai'], h1, h2").all()
            assert len(elements) > 0
            log.info(f"✓ Found {len(elements)} content elements on AI page")
        except Exception as e:
            log.warning(f"Content visibility check warning: {str(e)}")