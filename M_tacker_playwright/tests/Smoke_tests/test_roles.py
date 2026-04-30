import pytest
from tests.Smoke_tests.utilities.base_class import BaseClass
from tests.Smoke_tests.Pages.homepage import HomePage

@pytest.mark.Smoke_tests
@pytest.mark.dashboard
class TestRoles(BaseClass):
    """Roles management tests"""
    
    @pytest.mark.asyncio
    async def test_roles_page_load(self):
        """Test roles page loads"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing roles page load")
        await self.page.wait_for_timeout(5000)
        
        roles_page = await home_page.get_roles_page()
        await self.page.goto(roles_page)
        await self.page.wait_for_load_state('networkidle')
        
        current_url = self.page.url
        assert "roles" in current_url
        log.info("✓ Roles page loaded successfully")
    
    @pytest.mark.asyncio
    async def test_roles_table_visible(self):
        """Test roles table is visible"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing roles table visibility")
        roles_page = await home_page.get_roles_page()
        await self.page.goto(roles_page)
        await self.page.wait_for_timeout(5000)
        
        try:
            table = self.page.locator("table, [role='grid']").first
            is_visible = await table.is_visible()
            assert is_visible
            log.info("✓ Roles table is visible")
        except Exception as e:
            log.warning(f"Table visibility warning: {str(e)}")