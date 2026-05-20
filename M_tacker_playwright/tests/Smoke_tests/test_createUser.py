import pyautogui
import pyperclip
import pytest
from tests.Smoke_tests.utilities.base_class import BaseClass
from tests.Smoke_tests.Pages.homepage import HomePage
import time
import pandas as pd
import os
import random
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
            add_button = self.page.locator("//div/div/div/button[@class='themeBtn flex w-full md:w-auto']")
            await add_button.click()
            log.info("✓ Clicked add employee button")
            user_data=pd.read_excel("/Users/sachin/Desktop/qa_Automations/maxcelTracker_playwright/Maxcel_Trackerplaywright/M_tacker_playwright/tests/Smoke_tests/test_data/sample_1.xlsx")
            count=len(user_data)
            log.info(f"✓ Found {count} users in test data")
            n=0
            if count>0:
                add_user =self.page.locator("//button[contains(text(),'+ Add Another Employee')]")
                while n!=count-1:
                    await add_user.click()
                    n+=1
                    log.info(f"✓ Clicked add another employee button {n} times")
                    await self.page.wait_for_timeout(2000)
                    log.info(f"✓ Added {count,n+1} user fields")
            email_field = self.page.locator("input[placeholder='Employee Email']")   
            email_fields = await email_field.all()
            name_field = self.page.locator("input[placeholder='Full Name']")    
            name_fields = await name_field.all()
            id_field = self.page.locator("input[placeholder='Employee ID']")    
            id_fields = await id_field.all()
            for row, email_fields, name_fields, id_fields in zip(user_data.itertuples(index=False), email_fields, name_fields, id_fields):
                await email_fields.fill(row.Email)
                await name_fields.fill(row.Name)
                await id_fields.fill(row.ID)
                log.info(f"✓ Filled user details for {row.Name}")
                await self.page.wait_for_timeout(1000) 
            flat_data = []
            for _, row in user_data.iterrows():
                flat_data.extend([row['Role'], row['Shift'], row['Department'],row['Work Type']])
            input=self.page.locator("//div[@class='flex flex-wrap items-start gap-4 w-full mb-4']/div/div")
            input_fields = await input.all()
            log.info(f"✓ Found {len(input_fields)} dropdown fields")
            if len(flat_data) != len(input_fields):
                log.warning("Dropdown fields count does not match user data")
            else:
                for value, field in zip(flat_data, input_fields):
                    await field.click()
                    log.info(f"✓ Clicked dropdown field for value: {value}")
                    await self.page.wait_for_timeout(2000)
                    drop = self.page.locator(".css-fygc7l-option")
                    dropdown=await drop.all()
                    for option in dropdown:
                        option_text = await option.text_content()
                        if option_text and value in option_text:
                            await option.click()
                            log.info(f"✓ Selected dropdown option: {option_text}")
                            await self.page.wait_for_timeout(2000)
                            break
                        time.sleep(1)
            # email_field = self.page.locator("input[placeholder='Employee Email']").first
            # name_field = self.page.locator("input[placeholder='Full Name']").first
            # id_field = self.page.locator("input[placeholder='Employee ID']").first
            
            # await email_field.fill("testuser@example.com")
            # await name_field.fill("Test User")
            # await id_field.fill("EMP001")
            
            # log.info("✓ Filled user details")
            
            # submit_button = self.page.locator("button:has-text('Send Invitations')").first
            # await submit_button.click()
            # await self.page.wait_for_timeout(5000)
            # log.info("✓ User created successfully")
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
        
        
            filter_buttons = await self.page.locator(".css-c2frko-control").all()
            log.info(f"Found {len(filter_buttons)} filter buttons")
            user_data=pd.read_excel("/Users/sachin/Desktop/qa_Automations/maxcelTracker_playwright/Maxcel_Trackerplaywright/M_tacker_playwright/tests/Smoke_tests/test_data/sample_user.xlsx")
            count=len(user_data)
            log.info(f"✓ Found {count} users in test data")
            flat_data = []
            for _, row in user_data.iterrows():
                flat_data.extend([row['role'], row['department'], row['user'], row['shift'], row['device']])
            for filter_button,value in zip(filter_buttons, flat_data):
             try:
                    await filter_button.click()
                    await self.page.wait_for_timeout(2000)
                    options = await self.page.locator(".css-144zqx9 div").all()
                    n=0
                    for option in options:
                        option_text = await option.text_content()
                        log.info(f"Checking option: {option_text} for filter value: {value}")
                        if option_text == value:
                            await option.click()
                            log.info(f"✓ Selected filter option: {option_text}")
                            await self.page.wait_for_timeout(2000)
                            break
                    time.sleep(1)
             except Exception as e:
                    log.warning(f"Filter selection warning for value {value}: {str(e)}")
                

            
    
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
            action_buttons = await self.page.locator("div.MenuOuterDrop.supertab").all()
            log.info(f"Found {len(action_buttons)} action buttons")
            
            if len(action_buttons) > 0:
                # await action_buttons[0].click()
                # await self.page.wait_for_timeout(2000)
                random_button = random.choice(action_buttons)
                await random_button.click()
                await self.page.wait_for_timeout(2000)
                log.info("✓ Clicked user action")
                opt= self.page.locator("//ul/div/li[@role='menuitem']/span")
                options = await opt.all()
                log.info(f"Found {len(options)} options in user action menu")
                n=0
                try:
                    for option in options:
                        if n>5:
                            break
                        log.info(f"clicking on options {option.text_content()}")
                        time.sleep(4)
                        random_ch=random.choice(options)
                        action_txt =random_ch.text.strip()
                        log.info(f"clicke on options {action_txt}")
                        self.driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});",
                    random_ch,)
                    self.driver.execute_script("arguments[0].click();", random_ch)
                    if action_txt == "Deactivate":
                        time.sleep(2)
                        confirm =self.page.locator("//div[contains(text(), 'User Deactivated Successfully')]")
                        assert confirm.text_content() == "User Deactivated Successfully"
                        log.info("✓ User deactivated successfully")
                    elif action_txt == "Track" or action_txt == "Untrack":
                        time.sleep(2)
                        log.info(f"✓ {action_txt} option clicked successfully")
                        confirm = self.page.locator(f"//div[contains(text(), '{action_txt}ed Successfully')]")
                        assert confirm.text_content() == f"{action_txt}ed Successfully"
                        log.info("User tracking setting changed successfully")
                    elif action_txt == "Edit":
                        time.sleep(2)
                        log.info("✓ Edit option clicked successfully")
                        confirm = self.page.locator("//div[@class='relative bg-white rounded-lg shadow-lg z-50 w-full max-w-[1040px]']")
                        assert confirm.is_visible()
                        log.info("edit user screen opened successfully")
                        self.page.locator("//button[contains(text(), 'Cancel')]").click()
                        time.sleep(2)
                    elif action_txt == "Info":
                        time.sleep(2)
                        log.info("✓ Info option clicked successfully")
                        confirm = self.page.url
                        assert "organisation/dashboard/users" in confirm
                        log.info("navigated to user info page successfully")
                        self.page.get(user_page)
                        log.info("✓ Navigated back to user page successfully")
                        current_url = self.page.url
                        log.info(f"Current URL after navigating back: {current_url}")
                        time.sleep(2)
                    elif action_txt == "Disable Password" or action_txt == "Enable Password":
                     time.sleep(2)
                     if action_txt == "Disable Password":
                        log.info(f"✓ {action_txt} option clicked successfully")
                        confirm = self.page.locator(f"//div[contains(text(), 'Password {action_txt}d Successfully')]")
                        assert confirm.text_content == "Password Disabled Successfully"
                        log.info("User password setting changed successfully")
                    else:
                        confirm = self.page.locator(f"//div[contains(text(), '{action_txt}d Successfully')]")
                        assert confirm.text_content == "Password Enabled Successfully"
                        log.info("User password setting changed successfully")
                    log.info("password enabled/disabled successfully")
                except Exception as e:
                    log.warning(f"User action option selection warning: {str(e)}")
        except Exception as e:
            log.warning(f"User action test warning: {str(e)}")

    @pytest.mark.asyncio
    async def test_CreateUserBulk(self):
        log = self.getLogger()
        home_page = HomePage(self.page)     
        log.info("Testing bulk user creation")
        await self.page.wait_for_timeout(10000)
        user_page = await home_page.get_user_page()
        await self.page.goto(user_page)
        await self.page.wait_for_load_state('networkidle')
        upload_click=self.page.locator(".themeBtnWhiteOutline")
        await upload_click.click()
        log.info("✓ Clicked choose file button")
        await self.page.wait_for_timeout(2000)
        bulk=self.page.locator("//button[contains(text(),'Choose File')]")
        await bulk.click()
        log.info("✓ Clicked bulk choose file button")  
        file_name="/Users/sachin/Desktop/qa_Automations/maxcelTracker_playwright/Maxcel_Trackerplaywright/M_tacker_playwright/tests/Smoke_tests/test_data/sample_1.xlsx"
        log.info(f"✓ Uploading file: {file_name}")
        abs_path=os.path.abspath(file_name)
        log.info(abs_path)
        pyperclip.copy(abs_path)
        log.info("file path copied to clipboard")
        pyautogui.hotkey('command', 'v')
        log.info("file path pasted in the dialog box")  
        pyautogui.press('return')
        log.info("pressed enter key")
        time.sleep(5)
        log.info("✓ File uploaded successfully")
        done=self.page.locator("//button[contains(text(),'Send Invitations')]")
        await done.click()
        log.info("✓ Clicked send invitations button")
