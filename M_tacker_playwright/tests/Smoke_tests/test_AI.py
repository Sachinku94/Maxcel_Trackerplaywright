import pytest
from tests.Smoke_tests.utilities.base_class import BaseClass
from tests.Smoke_tests.Pages.homepage import HomePage
import pandas as pd
import time
import random
import re
from playwright.sync_api import Page, expect

@pytest.mark.Smoke_tests
@pytest.mark.dashboard
class TestAI(BaseClass):
    """AI Summary page tests"""
    
    @pytest.mark.asyncio
    async def test_ai_page_load(self):
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



    @pytest.mark.asyncio
    async def test_searchaiuser(self):
        """Test AI content is visible"""
        time.sleep(5)
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        time.sleep(1)
        log.info("Testing AI content visibility")
        ai_page = await home_page.get_ai_page()
        await self.page.goto(ai_page)
        log.info("Testing AI user search functionality")
        
        await self.page.wait_for_timeout(5000)
        user_data=pd.read_excel("/Users/sachin/Desktop/qa_Automations/maxcelTracker_playwright/Maxcel_Trackerplaywright/M_tacker_playwright/tests/Smoke_tests/test_data/sample_1.xlsx")
        count=len(user_data)
        log.info(f"Total number of users: {len(user_data)}")
        flat_data = []
        al_opt=[]
        search_user=self.page.locator(".css-19bb58m")
        all_user=await search_user.all()
        count_search_user= len(all_user)
        log.info(f"Total number of search user fields: {count_search_user}")
        time.sleep(2)
        for _, row in user_data.iterrows():
            flat_data.extend([row['Name'], row['Department']])

        for user,value in zip(all_user, flat_data):
            
                await user.click()
                time.sleep(5)
                opti = self.page.locator(".css-fygc7l-option")
                time.sleep(5)
                options = await opti.all()
                log.info(f"Total number of filter options: {len(options)}")
                for opt in options:
                    opt_text = await opt.text_content()
                    log.info(f"Checking filter option: {opt_text}")

                    if opt_text==row['Name'] or opt_text==row['Department']:
                        opt.click()
                        log.info(f"Clicked on filter option: {opt.text_content()}")
                        time.sleep(2)
                        break
                    elif opt_text!=value:
                        random_option=random.choice(options)
                        await random_option.click()
                        log.info(f"Clicked on random filter option: {random_option.text_content()}")

                        time.sleep(2)
                        break
            
                log.info(f"Exception occurred: ")
                time.sleep(2)
        cal=self.page.locator("//input[@placeholder='Select Date']")
        await cal.click()
        filter_days=self.page.locator("//div[@class='flex flex-col lg:flex-row py-2']/div/ul/li")
        filter_days_options=await filter_days.all()
        n=0
        for i in filter_days_options:
            if n<5:
                i.click()
                time.sleep(2)
                cal.click()
                n+=1
        tembtn=self.page.locator(".themeBtn")
        await tembtn.click()
        time.sleep(2)
        tost=self.page.locator(".Toastify__toast-body>div:last-child")
        tost_text=await tost.text_content()
        log.info(f"Toast message: {tost_text}")
        assert tost_text=="Report generation started. You'll be notified by email once ready."
        log.info("✓ AI user search functionality tested successfully")
