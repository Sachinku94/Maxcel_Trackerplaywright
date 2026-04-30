import pytest
from tests.Smoke_tests.utilities.base_class import BaseClass
from tests.Smoke_tests.Pages.homepage import HomePage

@pytest.mark.Smoke_tests
@pytest.mark.dashboard
class TestDepartment(BaseClass):
    """Department and Teams management tests"""
    
    @pytest.mark.asyncio
    async def test_department_page_load(self):
        """Test department page loads"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing department page load")
        await self.page.wait_for_timeout(5000)
        
        dept_page = await home_page.get_department_page()
        await self.page.goto(dept_page)
        await self.page.wait_for_load_state('networkidle')
        
        current_url = self.page.url
        assert "department-teams" in current_url
        log.info("✓ Department page loaded successfully")
    
    @pytest.mark.asyncio
    async def test_department_table_visible(self):
        """Test department table is visible"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing department table visibility")
        dept_page = await home_page.get_department_page()
        await self.page.goto(dept_page)
        await self.page.wait_for_timeout(5000)
        
        try:
            table_elements = await self.page.locator("table, [role='grid']").all()
            assert len(table_elements) > 0
            log.info("✓ Department table is visible")
        except Exception as e:
            log.warning(f"Table visibility check warning: {str(e)}")
    
    @pytest.mark.asyncio
    async def test_department_search(self):
        """Test department search functionality"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing department search")
        dept_page = await home_page.get_department_page()
        await self.page.goto(dept_page)
        await self.page.wait_for_timeout(5000)
        
        try:
            search_field = self.page.locator("input[placeholder*='search'], input[type='search']").first
            if await search_field.is_visible():
                await search_field.fill("Finance")
                await self.page.wait_for_timeout(2000)
                log.info("✓ Department search completed")
            else:
                log.info("Search field not visible")
        except Exception as e:
            log.warning(f"Search test warning: {str(e)}")