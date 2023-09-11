import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect
class opening_amazon_page:
    def run(self,playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False,timeout=30000)
        self.context = browser.new_context()
        self.page = self.context.new_page()
        self.page.goto("https://www.amazon.in/")

class testing_amazon_cart(opening_amazon_page):
    def searching_product(self,product_name):
        self.product_name=product_name
        self.page.locator("//input[@id='twotabsearchtextbox']").fill(self.product_name)
        self.page.locator("//input[@id='nav-search-submit-button']").click()

    def filtering_product_based_on_rating(self,rating):
        rating_box_path="(//li[@id='p_72/1318476031']/ancestor::ul)/descendant::li"
        all_rating_box=self.page.locator(rating_box_path)
        D={4:0,3:1,2:2,1:3}
        for k in D:
            if rating==k:
                all_rating_box.nth(D[k]).click()
                time.sleep(4)
                break

    def adding_to_cart_based_on_requirement(self,user_requirement_value):
        filtered_product_path="//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-2']/child::a"
        all_product_list=self.page.locator(filtered_product_path)
        count=0
        for i in range(all_product_list.count()):
            if count>user_requirement_value:
                break
            if re.search(self.product_name.split()[0],all_product_list.nth(i).inner_text()):

                time.sleep(8)
                with self.context.expect_page() as new_page_info:
                    all_product_list.nth(i).click()  # Opens a new tab
                new_page = new_page_info.value
                new_page.locator("//input[@id='add-to-cart-button']").click()
                time.sleep(3)
                new_page.close()
                self.page.reload()
            count += 1

    def checking_actual_price_and_summarised_price_are_same_or_not(self):
        actual_price = 0
        self.page.locator("//div[@id='nav-cart-count-container']").click()
        time.sleep(3)
        price_list = self.page.locator("//div[@class='sc-badge-price-to-pay']")
        for i in range(0,price_list.count()):
            print(price_list.nth(i).inner_text())
            actual_price += float(price_list.nth(i).inner_text().replace(',', ''))
        summarized_price = self.page.locator("(//span[@class='a-size-medium a-color-base sc-price sc-white-space-nowrap'])[1]").inner_text()
        print()
        print(summarized_price)
        print(actual_price)
        try:
            assert float(summarized_price.replace(',', '')) == actual_price, 'Cart Is Not Performing'
        except AssertionError as msg:
            print(msg)

with sync_playwright() as playwright:
    ob=testing_amazon_cart()
    ob.run(playwright)
    ob.searching_product('Dell Laptop')
    ob.filtering_product_based_on_rating(2)
    ob.adding_to_cart_based_on_requirement(3)
    ob.checking_actual_price_and_summarised_price_are_same_or_not()
