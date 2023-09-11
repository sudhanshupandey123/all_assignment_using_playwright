# # from playwright.async_api import async_playwright
# # import asyncio
# # async def opening_browser():
# #     p =await async_playwright().start()
# #     browser =await p.chromium.launch(
# #         headless=False,
# #     )
# #     return browser
# # async def main():
# #     abc = asyncio.run(opening_browser())
# #     page = abc.new_page()
# #     page.goto("http://www.google.com/")
# #     abc.close()
# # asyncio.run(main())
# #
# #
# #
# # import  asyncio
# # from playwright.async_api import async_playwright
# # async def main():
# #     async with async_playwright() as p:
# #         browser =  p.chromium.launch()
# #         page =  browser.new_page()
# #         return page
# # asyncio.run(main())
# import time
#
# # from playwright.async_api import async_playwright
# #
# # p=async_playwright().start()
# # p.chromium.launch(headless=False)
#
# from playwright.sync_api import Playwright, sync_playwright, expect
#
#
# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.google.com/maps/")
#     page.locator("//input[@id='searchboxinput']").fill('restaurant')
#     time.sleep(4)
#     page.locator("//button[@id='searchbox-searchbutton']").click()
#     time.sleep(5)
#     # ele=page.locator("//a[@class='hfpxzc']").all()
#     # print(ele)
#     for i in range(1,50):
#         try:
#             ele = page.locator("//a[@class='hfpxzc']").all()
#             ele[i].click()
#             time.sleep(5)
#         except IndexError:
#             page.keyboard.press('End')
#             time.sleep(5)
#             ele = page.locator("//a[@class='hfpxzc']").all()
#     print(len(ele))
#
#
#
#
#
#
#     # ---------------------
#     context.close()
#     browser.close()
#
#
# with sync_playwright() as playwright:
#     run(playwright)

count = 0
for i in range(1,10):
    count+=1

print(count)