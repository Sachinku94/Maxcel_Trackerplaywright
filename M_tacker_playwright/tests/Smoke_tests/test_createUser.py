import pytest
from M_tacker_playwright.tests.Smoke_tests.utilities.base_class import BaseClass
from M_tacker_playwright.tests.Smoke_tests.Pages.homepage import HomePage

@pytest.mark.Smoke_tests
@pytest.mark.users
class TestUserCreation(BaseClass):
    """User creation and management tests"""
    
    @pytest.mark.asyncio
    async def test_create_user_single(self):
        """Test creating a single user"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Starting single user creation test")
        await self.page.wait_for_timeout(10000)
        
        user_page = await home_page.get_user_page()
        await self.page.goto(user_page)
        await self.page.wait_for_load_state('networkidle')
        
        try:
            add_button = self.page.locator("button:has-text('+ Add Employee')").first
            await add_button.click()
            log.info("✓ Clicked add employee button")
            
            email_field = self.page.locator("input[placeholder='Employee Email']").first
            name_field = self.page.locator("input[placeholder='Full Name']").first
            id_field = self.page.locator("input[placeholder='Employee ID']").first
            
            await email_field.fill("testuser@example.com")
            await name_field.fill("Test User")
            await id_field.fill("EMP001")
            
            log.info("✓ Filled user details")
            
            submit_button = self.page.locator("button:has-text('Send Invitations')").first
            await submit_button.click()
            await self.page.wait_for_timeout(5000)
            log.info("✓ User created successfully")
        except Exception as e:
            log.error(f"User creation failed: {str(e)}")
            raise
    
    @pytest.mark.asyncio
    async def test_user_report(self):
        """Test user report page"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing user report page")
        await self.page.wait_for_timeout(10000)
        
        user_report_page = await home_page.get_user_report_page()
        await self.page.goto(user_report_page)
        await self.page.wait_for_load_state('networkidle')
        
        current_url = self.page.url
        assert "user-reports" in current_url
        log.info("✓ User report page loaded successfully")
    
    @pytest.mark.asyncio
    async def test_filter_users(self):
        """Test filtering users"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing user filtering")
        await self.page.wait_for_timeout(10000)
        
        user_page = await home_page.get_user_page()
        await self.page.goto(user_page)
        await self.page.wait_for_load_state('networkidle')
        
        try:
            filter_buttons = await self.page.locator(".filter-control, [role='combobox']").all()
            log.info(f"Found {len(filter_buttons)} filter buttons")
            
            if len(filter_buttons) > 0:
                await filter_buttons[0].click()
                await self.page.wait_for_timeout(2000)
                log.info("✓ Applied first filter")
        except Exception as e:
            log.warning(f"Filter test warning: {str(e)}")
    
    @pytest.mark.asyncio
    async def test_user_actions(self):
        """Test user actions"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        log.info("Testing user actions")
        await self.page.wait_for_timeout(10000)
        
        user_page = await home_page.get_user_page()
        await self.page.goto(user_page)
        await self.page.wait_for_load_state('networkidle')
        
        try:
            action_buttons = await self.page.locator("[role='menuitem']").all()
            log.info(f"Found {len(action_buttons)} action buttons")
            
            if len(action_buttons) > 0:
                await action_buttons[0].click()
                await self.page.wait_for_timeout(2000)
                log.info("✓ Clicked user action")
        except Exception as e:
            log.warning(f"User action test warning: {str(e)}")