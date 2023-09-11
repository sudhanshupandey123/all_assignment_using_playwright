# # from playwright.async_api import Page
# # from playwright.sync_api import Playwright, sync_playwright, expect
# # import time
# #
# # '''Function To get Xpath of User Interest City (Handling Dynamic Dropdowns)'''
# # # def get_path_of_city(city):
# # #     return f"//div[text()='{city}']"
# # import re
# #
# #
# # #
# # # def select_hover_ele(val):
# # #     return f"//div[@id='nav-al-your-account']//span[text()='{val}']"
# #
# # def run(playwright: Playwright) -> None:
# #     browser = playwright.chromium.launch(headless=False, slow_mo=10000)
# #     context = browser.new_context()
# #     page = context.new_page()
# # #
# # #
# # # """url-It is used to get the currnet url in playwright
# # #     go_back()-This Method is Used to go back from current url
# # #     go_forward()-This Method is Used to go forward from the current page"""
# #     page.goto("https://www.amazon.in/")
# #
# # with sync_playwright() as playwright:
# #     run(playwright)
# # # # print(page.url)
# # # # page.locator("//span[@id='nav-link-accountList-nav-line-1']").click()
# # # # print(page.url)
# # # # page.go_back()
# # # # print(page.url)
# # # # page.go_forward()
# # # # print(page.url)
# # # """
# # #     Filling And Clearing The Text"""
# # # # page.locator("//input[@id='twotabsearchtextbox']").fill('Amazon Laptop')
# # # # time.sleep(2)
# # # # #By Passing empty string again to same locators
# # # # page.locator("//input[@id='twotabsearchtextbox']").fill('')
# # # # time.sleep(2)
# # #
# # # '''
# # #     inner_text,text_content-Used to get the visisble text'''
# # # # print(page.locator("(//div[@id='nav-xshop']/child::a)[1]").inner_text())
# # # # print(page.locator("(//div[@id='nav-xshop']/child::a)[1]").text_content())
# # # #
# # # # '''input_value()-It is used to take out the text entered in input box'''
# # # # value=page.locator("//input[@id='twotabsearchtextbox']").fill('Dell Laptop')
# # # # print(page.locator("//input[@id='twotabsearchtextbox']").input_value())
# # #
# # # '''
# # #     Handling Dropdowns In Playwright By Selecting Single Value From Dropdowns'''
# # # # page.locator("//select[@id='searchDropdownBox']").select_option('Beauty')
# # #
# # # '''Handling Dropdowns In Playwright By Selecting Multiple Values From Dropdowns'''
# # # # page.locator("//select[@id='searchDropdownBox']").select_option(['Beauty','Amazon Fresh'])
# # #
# # # '''Selecting All Values From The Droopdown'''
# # # # all_values_of_dropdown=page.locator("//select[@id='searchDropdownBox']/child::option")
# # # # print(all_values_of_dropdown.count())
# # # # print(all_values_of_dropdown.all_inner_texts())
# # # # index=0
# # # # while index<all_values_of_dropdown.count():
# # # #     print(all_values_of_dropdown.nth(index).inner_text())
# # # #     page.locator("//select[@id='searchDropdownBox']").select_option(index=index)
# # # #     index+=1
# # #
# # # '''Handling Dynamic Dropdowns'''
# # # # page.goto('https://www.spicejet.com/')
# # # # input_box=page.locator("(//div[@class='css-1dbjc4n r-13awgt0 r-18u37iz']//input)[1]")
# # # # input_box.click()
# # # # input_box.fill('ag')
# # # # page.locator(get_path_of_city('Agra')).click()
# # #
# # # '''Selecting Element Contains Another Element'''
# # # # page.goto('https://www.amazon.in/')
# # # # all_nav=page.locator('div#nav-xshop',has=page.locator('a',has_text='Sell'))
# # # # print(all_nav.all_inner_texts())
# # #
# # # '''Hover Using Playwright'''
# # #
# # # # page.goto('https://amazon.in/')
# # # # hover_ele=page.locator("//span[@class='nav-line-2 ']")
# # # # hover_ele.hover()
# # # # all_ele_in_hover=page.locator("//div[@id='nav-al-your-account']//a")
# # # # print(all_ele_in_hover.all_inner_texts())
# # # # for i in all_ele_in_hover.all_inner_texts():
# # # #     all_ele_in_hover = page.locator("//div[@id='nav-al-your-account']//a")
# # # #     hover_ele.hover()
# # # #     page.locator(select_hover_ele(i)).click()
# # # #     page.go_back()
# # #
# # # '''Handling AutoSuggestion Dropdown'''
# # # # page.goto('https://demoqa.com/automation-practice-form')
# # # # page.locator("//input[@id='subjectsInput']").fill('e')
# # # # all_values_of_sugg=page.locator("//div[@class='subjects-auto-complete__menu-list subjects-auto-complete__menu-list--is-multi css-11unzgr']/child::div")
# # # # for i in all_values_of_sugg.all_inner_texts():
# # # #     if i=='Chemistry':
# # # #         page.locator(f"//*[text()='{i}']").click()
# # # '''Creating Function To Handle Auto Suggestion'''
# # # # def auto_suggestion_handling(input,subject):
# # # #     page.goto('https://demoqa.com/automation-practice-form')
# # # #     page.locator("//input[@id='subjectsInput']").fill(input)
# # # #     all_values_of_sugg = page.locator(
# # # #         "//div[@class='subjects-auto-complete__menu-list subjects-auto-complete__menu-list--is-multi css-11unzgr']/child::div")
# # # #     for i in all_values_of_sugg.all_inner_texts():
# # # #         if i == subject:
# # # #             page.locator(f"//*[text()='{i}']").click()
# # # # auto_suggestion_handling('p','Physics')
# # #
# # # '''Handling Iframes which don't have any id
# # #     Note: If iframe have no id we can use frame_locator() method to locate our iframe'''
# # # # page.goto('https://jqueryui.com/autocomplete/')
# # # # frame_locator=page.frame_locator("//iframe[@class='demo-frame']")
# # # # frame_locator.locator("//input[@id='tags']").fill('e')
# # #
# # # '''Handling Iframe which having id
# # #     Note: If iframe having id we can use frame() method to locate to our frame'''
# # # # page.goto('https://the-internet.herokuapp.com/iframe')
# # # # frame_locator=page.frame('mce_0_ifr')
# # # # frame_locator.locator("//*[@id='tinymce']").fill()
# # # # frame_locator.locator("//*[@id='tinymce']").type('Hi welcome to Iframes Concepts')
# # #
# # #
# # # '''
# # #     Handling Multiple Tabs In Playwright'''
# # # # page.goto('https://www.amazon.in')
# # # # page.locator("//input[@id='twotabsearchtextbox']").fill('Dell Laptop')
# # # # page.locator("//input[@type='submit']").click()
# # # # all_pro=page.locator("//span[@class='a-size-medium a-color-base a-text-normal']")
# # # # count=0
# # # # for i in range(all_pro.count()):
# # # #     if count==3:
# # # #         break
# # # #     all_pro.nth(i).click()
# # # #     count += 1
# # # # all_win=context.pages
# # # # for i in range(1,4):
# # # #     all_win[i].locator("//input[@id='add-to-cart-button']").click()
# # # #     all_win[i].locator("//span[@id='attach-sidesheet-view-cart-button']").click()
# # #
# # # '''Handling Javascripts Popups '''
# # # """Accepting The Alert"""
# # # # page.goto('https://the-internet.herokuapp.com/javascript_alerts')
# # # # page.locator("//li[1]//button").click()
# # # # page.on('dialog',lambda dialog:dialog.accept())
# # # # msg=page.locator("//p[@id='result']").inner_text()
# # # # assert msg =='You successfully clicked an alert','Not Showing The Correct Message'
# # #
# # # """Dismissing The alert
# # #     By Default Playwright will dismiss the alert"""
# # # # page.goto('https://the-internet.herokuapp.com/javascript_alerts')
# # # # page.locator("//li[2]//button").click()
# # # # msg = page.locator("//p[@id='result']").inner_text()
# # # # assert msg == 'You clicked: Cancel', 'Not Showing The Correct Message'
# # #
# # # '''Another Way to Dismiss the alert'''
# # # # page.goto('https://the-internet.herokuapp.com/javascript_alerts')
# # # # page.locator("//li[2]//button").click()
# # # # page.on('dialog',lambda dialog:dialog.dismiss())
# # # # msg = page.locator("//p[@id='result']").inner_text()
# # # # assert msg == 'You clicked: Cancel', 'Not Showing The Correct Message'
# # #
# # #
# # # '''Filling Text Into Alert'''
# # # # page.goto('https://the-internet.herokuapp.com/javascript_alerts')
# # # # page.locator("//li[3]//button").click()
# # # # time.sleep(2)
# # # # page.on('dialog', lambda dialog: dialog.accept('Automation'))
# # # # msg = page.locator("//p[@id='result']").inner_text()
# # # # assert msg == 'You entered: Automation', 'Not Showing The Correct Message'
# # #
# # # '''Handling Sweet Alerts'''
# # # # page.goto('https://sweetalert2.github.io/')
# # # # page.locator("//div[@class='showcase sweet']//button").click()
# # # # verifying_alert_opening=page.locator("//h2[@id='swal2-title']").inner_text()
# # # # assert verifying_alert_opening=='Good job!','Alert Is Not Opening'
# # # # page.locator("(//div[@class='swal2-loader']/following-sibling::button)[1]").click()
# # #
# # # '''Handling Drag And Drop In Playwright
# # #     Using drag_to()method'''
# # # # page.goto("https://the-internet.herokuapp.com/drag_and_drop")
# # # # src=page.locator("//*[@id='column-a']")
# # # # tar=page.locator("//*[@id='column-b']")
# # # # src.drag_to(tar)
# # # # print(page.locator("//*[@id='column-b']").inner_text())
# # #
# # # '''Another Way Of Doing Drag And Drop
# # #     Using drag_and_drop() method'''
# # # # page.goto("https://the-internet.herokuapp.com/drag_and_drop")
# # # # # src=page.locator("//*[@id='column-a']")
# # # # # tar=page.locator("//*[@id='column-b']")
# # # # page.drag_and_drop("//*[@id='column-a']","//*[@id='column-b']")
# # # # print(page.locator("//*[@id='column-b']").inner_text())
# # # #
# # # # def run(playwright: Playwright) -> None:
# # # #     browser = playwright.chromium.launch(headless=False, slow_mo=10000)
# # # #     context = browser.new_context()
# # # #     page = context.new_page()
# # # #     '''Handling Tooltip'''
# # #     # page.goto('https://jqueryui.com/tooltip/')
# # #     # frame_locator=page.frame_locator("//*[@class='demo-frame']")
# # #     # frame_locator.locator("//input[@id='age']").hover()
# # #     # msg=frame_locator.locator("//div[@class='ui-tooltip-content']").inner_text()
# # #     # assert msg=="We ask for your age only for statistical purposes.",'Tooltip Not Working'
# # #     # '''Handling Horizontal Slider'''
# # #     # page.goto("https://the-internet.herokuapp.com/horizontal_slider")
# # #     # slider=page.locator("//input[@type='range']")
# # #     # slider_range=page.locator("//span[@id='range']")
# # #     # slider.click()
# # #     # user_range=3.5
# # #     # while float(slider_range.inner_text())<user_range:
# # #     #     slider.press('ArrowRight')
# # #     # print(slider_range.inner_text())
# # #
# # #     '''Handling Toast Messages'''
# # #     # page.goto('https://codeseven.github.io/toastr/demo.html')
# # #     # page.locator("//button[@id='showtoast']").click()
# # #     # print(page.locator("//div[@class='toast toast-success']//div").inner_text())
# # #
# # # #     '''Uploading Files'''
# # # #     page.goto('https://davidwalsh.name/demo/multiple-file-upload.php')
# # # #
# # # #     # page.set_input_files("//div[@class='ZeVBtc']//span","C:\\Users\\a98016117\\Downloads\\download.jfif")
# # # #     page.locator("//input[@type='file']").set_input_files("C:\\Users\\a98016117\\Downloads\\download.jfif")
# # # #
# # # #
# # # # with sync_playwright() as playwright:
# # # #     run(playwright)
# # # #
# # # from playwright.sync_api import sync_playwright
# # #
# # # def run(playwright):
# # #     chrome = playwright.chromium
# # #     browser = chrome.launch()
# # #     page = browser.new_page()
# # #     page.goto("https://example.com")
# # #     browser.close()
# # #
# # # with sync_playwright() as playwright:
# # #     run(playwright)
# # #
# # # import playwright
# # #
# # # browser=playwright.chromium.launch(headless=False, slow_mo=10000)
# # # class start:
# # #     def run(playwright: Playwright) -> None:
# # #         browser = playwright.chromium.launch(headless=False, slow_mo=10000)
# # #         context = browser.new_context()
# # #         page = context.new_page()
# #
# #
# # #
# # # from playwright.async_api import async_playwright
# # # async def browser_chrome():
# # #     p=async_playwright().start()
# # #     browser=p.chromium.launch(headless=True)
# # #     page=browser.new_page()
# # #     return page
# #
# # # class open_page:
# # #     def run(playwright: Playwright) -> None:
# # #
# # #         browser = playwright.chromium.launch(headless=False, slow_mo=10000)
# # #         context = browser.new_context()
# # #         page = context.new_page()
# # #         page.goto('https://www.google.com')
# # # ob=open_page()
# # # ob.run()
# import time
#
# from playwright.sync_api import Playwright, sync_playwright, expect
#
# class start_playwright:
#     def run(self,playwright: Playwright) -> None:
#         browser = playwright.chromium.launch(headless=False,timeout=30000)
#         context = browser.new_context()
#         self.page = context.new_page()
#         self.page.goto("https://www.amazon.in/")
#
#     def enter_product_details(self):
#         self.page.locator("//input[@id='twotabsearchtextbox']").fill('Dell Laptop')
#         time.sleep(3)
#
#
#
#
# # with sync_playwright() as playwright:
# #     run(playwright)