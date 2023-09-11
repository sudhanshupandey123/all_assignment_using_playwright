import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect
class opening_google_map:
    def run(self,playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False,timeout=30000)
        self.context = browser.new_context()
        self.page = self.context.new_page()
        self.page.goto("https://www.google.com/maps/")

class testing_google_map(opening_google_map):
    def searching_element_on_map(self,element_name):
        self.page.locator("//input[@id='searchboxinput']").fill(element_name)
        self.page.locator("//input[@id='searchboxinput']").press('Enter')
        time.sleep(5)
    def extracting_details(self):
        # time.sleep(5)


        # print(search_list.count())
        for i in range(1,50):
            search_list = self.page.locator("//div[@class='Nv2PK THOPZb CpccDe ']//a")
            self.page.keyboard.press('End')
            time.sleep(5)
        print(search_list.count())



with sync_playwright() as playwright:
    ob=testing_google_map()
    ob.run(playwright)
    ob.searching_element_on_map('Restaurant')
    ob.extracting_details()
