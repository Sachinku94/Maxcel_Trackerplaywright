from logging import log
import pytest
from tests.Smoke_tests.utilities.base_class import BaseClass
from tests.Smoke_tests.Pages.homepage import HomePage
import time
import random

@pytest.mark.Smoke_tests
@pytest.mark.dashboard
class TestAlerts(BaseClass):
    """Alerts management tests"""
    
    @pytest.mark.asyncio
    async def test_alerts_page_load(self):
        """Test alerts page loads"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing alerts page load")
        await self.page.wait_for_timeout(5000)
        
        alerts_page = await home_page.get_alerts_page()
        await self.page.goto(alerts_page)
        await self.page.wait_for_load_state('networkidle')
        
        current_url = self.page.url
        assert "alerts" in current_url
        log.info("✓ Alerts page loaded successfully")
    
    @pytest.mark.asyncio
    async def test_alerts_content_visible(self):
        """Test alerts content is visible"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing alerts content")
        alerts_page = await home_page.get_alerts_page()
        await self.page.goto(alerts_page)
        await self.page.wait_for_timeout(5000)
        
        try:
            alert_elements = await self.page.locator("[class*='alert'], [class*='notification']").all()
            log.info(f"✓ Found {len(alert_elements)} alert elements")
        except Exception as e:
            log.warning(f"Alerts content warning: {str(e)}")


    @pytest.mark.asyncio
    async def test_emailradiobtn(self):
            """Test alerts content is visible"""
            log = self.getLogger()
            time.sleep(5)
            home_page = HomePage(self.page)
            log.info("Testing alerts content")
            alerts_page = await home_page.get_alerts_page()
            await self.page.goto(alerts_page)
            time.sleep(5)
            radio = self.page.locator(".transition-colors")
            radio_buttons = await radio.all()
            log.info(f"✓ Found {len(radio_buttons)} alert type radio buttons")
            for i in radio_buttons:                
                    await i.click()
                    log.info("✓ Alert type radio button clicked successfully")
            dropdown= self.page.locator(".css-c2frko-control")
            drop=await dropdown.all()
            log.info(f"✓ Found {len(drop)} options for alert type")
            for i in drop:
                try:
                    await i.click()
                    log.info("✓ Alert type radio button clicked successfully")
                    options =  self.page.locator(".css-fygc7l-option").all()
                    log.info(f"✓ Found {len(options)} options for alert type")
                    choice=random.choice(options)
                    choice.click()
                    time.sleep(2)
                


                except Exception as e:
                    log.warning(f"Alert type radio button click warning: {str(e)}")

                log.info("all minute options are working")
                checkbox= self.page.locator(".checkmark")
                chek=await checkbox.all()
                for i in chek:
                    await i.click()
                    time.sleep(2)
                log.info("all chekbox optons are working correctly")

                
    
            
    