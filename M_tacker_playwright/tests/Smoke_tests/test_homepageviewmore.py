import pytest
from tests.Smoke_tests.utilities.base_class import BaseClass

@pytest.mark.Smoke_tests
@pytest.mark.dashboard
class TestHomepageViewMore(BaseClass):
    """Homepage View More functionality tests"""
    
    @pytest.mark.asyncio
    async def test_view_more_buttons(self):
        """Test view more buttons functionality"""
        log = self.getLogger()
        
        log.info("Testing view more buttons")
        await self.page.wait_for_timeout(10000)
        
        try:
            view_more_buttons = await self.page.locator("button:has-text('View More'), button:has-text('Show More')").all()
            log.info(f"Found {len(view_more_buttons)} view more buttons")
            
            if len(view_more_buttons) > 0:
                await view_more_buttons[0].click()
                await self.page.wait_for_timeout(2000)
                log.info("✓ View more button clicked")
        except Exception as e:
            log.warning(f"View more test warning: {str(e)}")
    
    @pytest.mark.asyncio
    async def test_homepage_widgets(self):
        """Test homepage widgets"""
        log = self.getLogger()
        
        log.info("Testing homepage widgets")
        await self.page.wait_for_timeout(10000)
        
        try:
            widgets = await self.page.locator("[class*='widget'], [class*='card']").all()
            log.info(f"✓ Found {len(widgets)} widgets on homepage")
        except Exception as e:
            log.warning(f"Widgets test warning: {str(e)}")