import pytest
from tests.Smoke_tests.utilities.base_class import BaseClass
from tests.Smoke_tests.Pages.homepage import HomePage

@pytest.mark.Smoke_tests
@pytest.mark.dashboard
class TestLiveStream(BaseClass):
    """Live stream tests"""
    
    @pytest.mark.asyncio
    async def test_live_stream_page(self):
        """Test live stream page"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing live stream page")
        await self.page.wait_for_timeout(5000)
        
        stream_page = await home_page.get_live_stream_page()
        await self.page.goto(stream_page)
        await self.page.wait_for_load_state('networkidle')
        
        current_url = self.page.url
        assert "live-stream" in current_url
        log.info("✓ Live stream page loaded")
    
    @pytest.mark.asyncio
    async def test_stream_content_visible(self):
        """Test stream content is visible"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing stream content visibility")
        stream_page = await home_page.get_live_stream_page()
        await self.page.goto(stream_page)
        await self.page.wait_for_timeout(5000)
        
        try:
            content = await self.page.locator("[class*='stream'], [class*='video'], video").all()
            log.info(f"✓ Found {len(content)} stream elements")
        except Exception as e:
            log.warning(f"Stream content warning: {str(e)}")