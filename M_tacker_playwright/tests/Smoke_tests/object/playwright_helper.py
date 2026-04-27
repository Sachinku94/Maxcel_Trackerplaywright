import logging
import inspect
from playwright.async_api import Page
import asyncio
import aiohttp
import requests
from typing import List, Set

class PlaywrightHelper:
    """Helper class for Playwright-specific operations"""
    
    def __init__(self, page: Page):
        self.page = page
    
    def getLogger(self):
        """Get logger instance"""
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        
        if not logger.handlers:
            file_handler = logging.FileHandler("logfile.log")
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
            )
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            logger.setLevel(logging.DEBUG)
        
        return logger
    
    async def fetch_css_properties_for_element(self, element, css_properties_list: List[str]) -> Set[str]:
        """Fetch CSS properties for a given element"""
        properties = set()
        for prop in css_properties_list:
            try:
                value = await element.evaluate(f"el => window.getComputedStyle(el).{prop}")
                if value:
                    properties.add(str(value))
            except:
                pass
        return properties
    
    async def fetch_and_check_css_properties(
        self, css_selector: str, expected_css_properties: Set[str], css_properties_list: List[str]
    ) -> bool:
        """Fetch and check CSS properties for elements"""
        try:
            elements = await self.page.locator(css_selector).all()
            fetched_properties = set()
            
            for element in elements:
                props = await self.fetch_css_properties_for_element(element, css_properties_list)
                fetched_properties.update(props)
                
                if fetched_properties == expected_css_properties:
                    return True
            
            return fetched_properties == expected_css_properties
        except Exception as e:
            logging.error(f"Error checking CSS properties: {str(e)}")
            return False
    
    async def verify_links(self, selectors: List[str], additional_links: List[str] = None) -> bool:
        """Verify that all links are accessible (not 404)"""
        log = self.getLogger()
        all_links = []
        
        for selector in selectors:
            try:
                elements = await self.page.locator(selector).all()
                for element in elements:
                    href = await element.get_attribute('href')
                    if href:
                        all_links.append(href)
            except Exception as e:
                log.error(f"Error extracting links from {selector}: {str(e)}")
        
        if additional_links:
            all_links.extend(additional_links)
        
        broken_links = []
        for link in all_links:
            try:
                response = requests.head(link, timeout=5, allow_redirects=True)
                if response.status_code == 404:
                    log.error(f"Broken link: {link} (404)")
                    broken_links.append(link)
            except Exception as e:
                log.error(f"Error checking link {link}: {str(e)}")
                broken_links.append(link)
        
        return len(broken_links) == 0
    
    async def verify_links_async(self, selectors: List[str]) -> bool:
        """Asynchronously verify all links are accessible"""
        log = self.getLogger()
        all_links = []
        
        for selector in selectors:
            try:
                elements = await self.page.locator(selector).all()
                for element in elements:
                    href = await element.get_attribute('href')
                    if href:
                        all_links.append(href)
            except Exception as e:
                log.error(f"Error extracting links: {str(e)}")
        
        async with aiohttp.ClientSession() as session:
            tasks = []
            for link in all_links:
                tasks.append(self._check_link_async(session, link, log))
            results = await asyncio.gather(*tasks)
        
        return all(result for result in results)
    
    async def _check_link_async(self, session, link: str, log) -> bool:
        """Check if link is accessible asynchronously"""
        try:
            async with session.head(link, timeout=aiohttp.ClientTimeout(total=5), allow_redirects=True) as response:
                if response.status == 404:
                    log.error(f"Link {link} is broken (404)")
                    return False
                return True
        except Exception as e:
            log.error(f"Error checking link {link}: {str(e)}")
            return False