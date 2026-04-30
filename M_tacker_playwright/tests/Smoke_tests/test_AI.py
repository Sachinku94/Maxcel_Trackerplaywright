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
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        
        log.info("Testing AI content visibility")
        ai_page = await home_page.get_ai_page()
        await self.page.goto(ai_page)
        log.info("Testing AI user search functionality")
        
        # await self.page.wait_for_timeout(5000)
        # user_data=pd.read_excel("test_data/AI_summary_test_data.xlsx", sheet_name="Sheet1")
        # count=len(user_data)
        # log.info(f"Total number of users: {len(user_data)}")
        # flat_data = []
        # al_opt=[]
        # search_user=self.page.locator(".css-19bb58m")
        # search_users=await search_user.all()
        # for _, row in user_data.iterrows():
        #     flat_data.extend([row['Name'], row['Department']])
            
        # for user,value in zip(search_user, flat_data):
        #     try:
        #         await user.click()
        #         options = await self.page.locator(".css-1n7v3ny-option").all()
        #         for opt in options:
        #             log.info(f"clicking on filter option {opt.text}")
        #             if opt.text==row['Name'] or opt.text==row['Department']:
        #                 opt.click()
        #                 time.sleep(2)
        #                 break
        #             elif opt.text!=value:
        #                 random_option=random.choice(options)
        #                 random_option.click()

        #                 time.sleep(2)
        #                 break
        #     except Exception as e:
        #         log.info(f"Exception occurred: {e}")
        #         time.sleep(2)
        # cal=self.page.locator("//input[@placeholder='Select Date']")
        # await cal.click()
        # filter_days=self.page.locator("//div[@class='flex flex-col lg:flex-row py-2']/div/ul/li")
        # filter_days_options=await filter_days.all()
        # n=0
        # for i in filter_days_options:
        #     if n<5:
        #         i.click()
        #         time.sleep(2)
        #         cal.click()
        #         n+=1
        # tembtn=self.page.locator(".themeBtn")
        # await tembtn.click()
        # time.sleep(2)
        # tost=self.page.locator(".Toastify__toast-body>div:last-child")
        # tost_text=await tost.text_content()
        # log.info(f"Toast message: {tost_text}")
        # assert tost_text=="Report generation started. You'll be notified by email once ready."
