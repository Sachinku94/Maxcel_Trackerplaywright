import pytest
from M_tacker_playwright.tests.Smoke_tests.utilities.base_class import BaseClass
from M_tacker_playwright.tests.Smoke_tests.Pages.homepage import HomePage

@pytest.mark.Smoke_tests
@pytest.mark.oauth
class TestOAuth(BaseClass):
    """OAuth and Authorization test cases"""
    
    @pytest.mark.asyncio
    async def test_scope_injection(self):
        """Test OAuth scope injection"""
        log = self.getLogger()
        
        injected_scope_url = (
            "https://accounts.google.com/o/oauth2/v2/auth?"
            "client_id=10422792105-51naiajknd89lhdt1g4r74jp2o42cl73.apps.googleusercontent.com&"
            "redirect_uri=https%3A%2F%2Fstg-fe.maxeltracker.com%2Fapi%2Fauth%2Fgoogle%2Fcallback&"
            "response_type=code&"
            "scope=openid%20email%20profile%20https://www.googleapis.com/auth/admin.directory.user&"
            "access_type=offline&"
            "prompt=consent"
        )
        
        log.info("Testing scope injection")
        await self.page.goto(injected_scope_url)
        await self.page.wait_for_timeout(5000)
        
        current_url = self.page.url
        assert "error" in current_url or "consent" in current_url
        log.info("✓ Scope injection test passed")
    
    @pytest.mark.asyncio
    async def test_redirect_uri_manipulation(self):
        """Test redirect URI manipulation"""
        log = self.getLogger()
        
        tampered_url = (
            "https://accounts.google.com/o/oauth2/v2/auth?"
            "client_id=10422792105-51naiajknd89lhdt1g4r74jp2o42cl73.apps.googleusercontent.com&"
            "redirect_uri=https%3A%2F%2Fevil.com%2Fcallback&"
            "response_type=code&"
            "scope=openid%20email%20profile&"
            "access_type=offline&"
            "prompt=consent"
        )
        
        log.info("Testing redirect URI manipulation")
        await self.page.goto(tampered_url)
        await self.page.wait_for_timeout(5000)
        
        current_url = self.page.url
        assert "error" in current_url or "redirect_uri_mismatch" in current_url
        log.info("✓ Redirect URI test passed")
    
    @pytest.mark.asyncio
    async def test_authorization(self):
        """Test authorization for limited user"""
        log = self.getLogger()
        home_page = HomePage(self.page)
        
        await self.page.wait_for_timeout(10000)
        
        try:
            user_profile = self.page.locator("#sidebar-profile-txt").first
            user_name = await user_profile.text_content()
            log.info(f"Current user: {user_name}")
            
            if user_name == "Akash Sharma":
                restricted_pages = [
                    await home_page.get_kpi_page(),
                    await home_page.get_apps_and_websites_page(),
                    await home_page.get_roles_page(),
                    await home_page.get_screen_record_page()
                ]
                
                for page_url in restricted_pages:
                    await self.page.goto(page_url)
                    await self.page.wait_for_timeout(5000)
                    current_url = self.page.url
                    assert "access-denied" in current_url or "access_denied" in current_url
                    log.info(f"✓ Access correctly denied for {page_url}")
            else:
                log.info(f"User {user_name} doesn't have limited access, skipping")
        except Exception as e:
            log.error(f"Authorization test failed: {str(e)}")
            raise