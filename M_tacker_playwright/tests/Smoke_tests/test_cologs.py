import pytest
from tests.Smoke_tests.utilities.base_class import BaseClass
from tests.Smoke_tests.Pages.homepage import HomePage
import time
import pandas as pd
import random
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

    @pytest.mark.asyncio
    async def test_logs_calendar(self):
        """Test logs calendar filter options are visible and clickable"""
        log = self.getLogger()
        home_page = HomePage(self.page)

        log.info("Testing logs calendar filter options")
        logs_page = await home_page.get_comprehensive_logs_page()
        await self.page.goto(logs_page)
        await self.page.wait_for_timeout(5000)

        calendar = self.page.locator("//input[@placeholder='Select Date']")
        is_visible = await calendar.is_visible()
        assert is_visible
        log.info("✓ Logs calendar is visible")
        await calendar.click()
        filter_days = self.page.locator("//div[@class='flex flex-col lg:flex-row py-2']/div/ul/li")
        filter_days_count = await filter_days.count()
        log.info(f"✓ Found {filter_days_count} filter options in calendar")
        filters_days = await filter_days.all()
        for i in filters_days:
            try:
                await i.click()
                log.info("✓ Calendar filter option clicked successfully")
                await calendar.click()  # Reopen calendar for next option
            except Exception as e:
                log.warning(f"Calendar filter click warning: {str(e)}")
                await calendar.click()  # Reopen calendar for next option

    @pytest.mark.asyncio
    async def test_logsfilterco(self):
        """Test filtering logs"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing logs filtering")
        await self.page.wait_for_timeout(10000)
        
        user_page = await home_page.get_comprehensive_logs_page()
        await self.page.goto(user_page)
        await self.page.wait_for_load_state('networkidle')
        
        time.sleep(5)
        user_data=pd.read_excel("/Users/sachin/Desktop/qa_Automations/maxcelTracker_playwright/Maxcel_Trackerplaywright/M_tacker_playwright/tests/Smoke_tests/test_data/sample_1.xlsx")
        count=len(user_data)
        log.info(f"✓ Found {count} users in test data")
        flat_data = []
        al_opt=[]
        filter_but= self.page.locator(".css-19bb58m")
        filter_buttons = await filter_but.all()
        for _, row in user_data.iterrows():
            flat_data.extend([row['Department'], row['Name']])
        log.info(f"✓ Flattened user data: {flat_data}")
        for value, field in zip(flat_data, filter_buttons):
            await field.click()
            log.info(f"✓ Clicked filter button for value: {value}")
            await self.page.wait_for_timeout(2000)
            drop = self.page.locator(".css-fygc7l-option")
            dropdown=await drop.all()
            for option in dropdown:
                option_text = await option.text_content()
                if option_text and value in option_text:
                    await option.click()
                    log.info(f"✓ Selected filter option: {option_text}")
                    await self.page.wait_for_timeout(2000)
                    break
                time.sleep(1)
        log.info(f"✓ Completed logs filtering test: {value}")

    @pytest.mark.asyncio
    async def test_logsdatewise(self):   
        """Test filtering logs datewise"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing logs datewise filtering")
        await self.page.wait_for_timeout(10000)
        
        user_page = await home_page.get_comprehensive_logs_page()
        await self.page.goto(user_page)
        await self.page.wait_for_load_state('networkidle')
        
        filter_but= self.page.locator(".css-c2frko-control")
   
        filter_buttons = await filter_but.all()
        for i in filter_buttons:
            try:
                await i.click()
                log.info("✓ Clicked date filter dropdown")
                await self.page.wait_for_timeout(2000)
                drop = self.page.locator(".css-fygc7l-option")
                dropdown=await drop.all()
                for option in dropdown:
                    option_text = await option.text_content()
                    log.info(f"Checking date filter option: {option_text}")
                    if option_text and "Last 7 days" in option_text:
                        await option.click()
                        log.info(f"✓ Selected date filter option: {option_text}")
                        await self.page.wait_for_timeout(2000)
                        break
            except Exception as e:
                log.warning(f"Date filter click warning: {str(e)}")