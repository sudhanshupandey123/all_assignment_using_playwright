from P1 import *
start=start_playwright()
with sync_playwright() as playwright:
    start.run(playwright)
    start.enter_product_details()