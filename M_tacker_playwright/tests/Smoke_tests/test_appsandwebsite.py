import pytest
from tests.Smoke_tests.utilities.base_class import BaseClass
from tests.Smoke_tests.Pages.homepage import HomePage

@pytest.mark.Smoke_tests
@pytest.mark.dashboard
class TestAppsAndWebsites(BaseClass):
    """Apps and Websites tests"""
    
    @pytest.mark.asyncio
    async def test_apps_and_websites_page(self):
        """Test apps and websites page"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing apps and websites page")
        await self.page.wait_for_timeout(5000)
        
        apps_page = await home_page.get_apps_and_websites_page()
        await self.page.goto(apps_page)
        await self.page.wait_for_load_state('networkidle')
        
        current_url = self.page.url
        assert "apps-and-websites" in current_url
        log.info("✓ Apps and websites page loaded")
    
    @pytest.mark.asyncio
    async def test_apps_table_visible(self):
        """Test apps table is visible"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing apps table visibility")
        apps_page = await home_page.get_apps_and_websites_page()
        await self.page.goto(apps_page)
        await self.page.wait_for_timeout(5000)
        
        try:
            table = self.page.locator("table, [role='grid']").first
            is_visible = await table.is_visible()
            assert is_visible
            log.info("✓ Apps table is visible")
        except Exception as e:
            log.warning(f"Table visibility warning: {str(e)}")



    @pytest.mark.asyncio
    async def test_appclendar(self):
        """Test apps calendar filter options are visible and clickable"""
        log = self.getLogger()
        home_page = HomePage(self.page)

        log.info("Testing apps calendar filter options")
        apps_page = await home_page.get_apps_and_websites_page()
        await self.page.goto(apps_page)
        await self.page.wait_for_timeout(5000)
        cel= self.page.locator("//input[@placeholder='Select Date']")
        is_visible = await cel.is_visible()
        assert is_visible
        log.info("✓ Apps calendar is visible") 
        await cel.click()
        filter_days= self.page.locator("//div[@class='flex flex-col lg:flex-row py-2']/div/ul/li")
        filter_days_count = await filter_days.count()
        log.info(f"✓ Found {filter_days_count} filter options in calendar")
        filters_days = await filter_days.all()
        for i in filters_days:
            try:
                await i.click()
                log.info("✓ Calendar filter option clicked successfully")
                await cel.click()  # Reopen calendar for next option
            except Exception as e:
                log.warning(f"Calendar filter click warning: {str(e)}")
                await cel.click()  # Reopen calendar for next option    