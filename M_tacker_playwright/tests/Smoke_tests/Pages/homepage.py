from tests.Smoke_tests.utilities.base_class import BaseClass
from Config.config_reader import read_config
from playwright.async_api import Page

class HomePage(BaseClass):
    """HomePage Page Object Model"""
    
    def __init__(self, page: Page):
        self.page = page
        self.env_url = read_config("env", "stg_url")
    
    async def get_user_page(self) -> str:
        await self.page.wait_for_timeout(5000)
        return self.env_url + "organisation/dashboard/users"
    
    async def get_user_report_page(self) -> str:
        await self.page.wait_for_timeout(5000)
        return self.env_url + "organisation/dashboard/user-reports"
    
    async def get_apps_and_websites_page(self) -> str:
        await self.page.wait_for_timeout(5000)
        return self.env_url + "organisation/dashboard/apps-and-websites"
    
    async def get_screenshot_page(self) -> str:
        await self.page.wait_for_timeout(5000)
        return self.env_url + "organisation/dashboard/screenshots"
    
    async def get_graph_logs_page(self) -> str:
        await self.page.wait_for_timeout(5000)
        return self.env_url + "organisation/dashboard/logs/log-by-chart"
    
    async def get_comprehensive_logs_page(self) -> str:
        await self.page.wait_for_timeout(5000)
        return self.env_url + "organisation/dashboard/logs/log-by-date"
    
    async def get_productivity_page(self) -> str:
        await self.page.wait_for_timeout(5000)
        return self.env_url + "organisation/dashboard/productivity/most-productive"
    
    async def get_unproductive_page(self) -> str:
        await self.page.wait_for_timeout(5000)
        return self.env_url + "organisation/dashboard/productivity/most-unproductive"
    
    async def get_idle_page(self) -> str:
        await self.page.wait_for_timeout(5000)
        return self.env_url + "organisation/dashboard/productivity/most-idle"
    
    async def get_best_performer_page(self) -> str:
        await self.page.wait_for_timeout(5000)
        return self.env_url + "organisation/dashboard/productivity/best-performance"
    
    async def get_department_page(self) -> str:
        await self.page.wait_for_timeout(5000)
        return self.env_url + "organisation/dashboard/department-teams"
    
    async def get_kpi_page(self) -> str:
        await self.page.wait_for_timeout(5000)
        return self.env_url + "organisation/dashboard/kpis-kras"
    
    async def get_roles_page(self) -> str:
        await self.page.wait_for_timeout(5000)
        return self.env_url + "organisation/dashboard/roles"
    
    async def get_live_stream_page(self) -> str:
        await self.page.wait_for_timeout(5000)
        return self.env_url + "organisation/dashboard/live-stream"
    
    async def get_screen_record_page(self) -> str:
        await self.page.wait_for_timeout(5000)
        return self.env_url + "organisation/dashboard/video-recording"
    
    async def get_alerts_page(self) -> str:
        await self.page.wait_for_timeout(5000)
        return self.env_url + "organisation/dashboard/alerts"
    
    async def get_ai_page(self) -> str:
        await self.page.wait_for_timeout(5000)
        return self.env_url + "organisation/dashboard/ai-summary"
    
    async def get_settings_page(self) -> str:
        await self.page.wait_for_timeout(5000)
        return self.env_url + "organisation/dashboard/settings"