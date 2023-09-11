from behave import *
from playwright.sync_api import sync_playwright
import time
import re
'''Opening Playwright And Chrome Browser To Perform The Task'''
p = sync_playwright().start()
browser = p.chromium.launch(headless=False)


'''After Completion of All Scenario Closing Windows And Page'''
def after_scenario(context):
    context.tab.close()
    context.page.close()
    browser.close()

paths = {
    'search_box_xpath': "//input[@id='searchboxinput']",
    'searched_interest_list_xpath': "//*[@class='Nv2PK THOPZb CpccDe ']/child::a",
    'restaurant_name_xpath': "//h1[@class='DUwDvf lfPIob']",
    'restaurant_rating_xpath': "//span[@class='ceNzKf']/preceding-sibling::span",
    'restaurants_address_xpath': "(//div[@class='rogA2c ']/child::div)[1]",
    'restaurant_review_xpath': "(//div[@class='F7nice ']/child::span)[2]",
    # "//*[@class='Nv2PK THOPZb CpccDe ']/child::a"
}
@given(u'He Open Google Map')
def opening_google_map(context):
    '''Opening Amazon Page'''
    context.tab = browser.new_context()
    context.page = context.tab.new_page()
    context.page.goto("http://www.google.com/maps/.in/")


@when(u'He Search For "restaurant near marathahalli"')
def searching_for_inforamtion(context):
    context.page.locator("//input[@id='searchboxinput']").fill('restaurant')
    time.sleep(4)
    context.page.locator("//button[@id='searchbox-searchbutton']").click()
    time.sleep(5)
@when(u'He Save Top "5" All The Details')
def Extracting_Information(context):
    context.D={}
    context.details=[]
    for i in range(0,50):
        try:
            ele = context.page.locator("//a[@class='hfpxzc']").all()
            ele[i].click()
            try:
                context.D['name'] = context.page.locator(paths['restaurant_name_xpath']).text
            except:
                context.D['name'] = 'NULL'

            try:
                context.D['rating'] = context.page.locator(paths['restaurant_rating_xpath']).text_content()
            except:
                context.D['rating'] = 'NULL'

            try:
                context.D['address'] = context.page.locator(paths['restaurants_address_xpath']).text_content()
            except:
                context.D['address'] = 'NULL'

            try:
                context.D['review'] = context.page.locator(paths['restaurant_review_xpath']).text_content()
            except:
                context.D['review'] = 'NULL'
            try:
                url = str(context.page.url)
                filtering_lat_and_long = re.search('@\d+\S{1}\d+,\d+\S{1}\d+', url)
                context.D['Log_and_Lat'] = filtering_lat_and_long.group()
                context.D['Log_and_Lat'] = context.D['Log_and_Lat'].replace('@', '')
            except:
                context.D['Log_and_Lat'] = 'NULL'


        except IndexError:
            context.page.keyboard.press('End')
            time.sleep(5)
            ele = context.page.locator("//a[@class='hfpxzc']").all()
        context.details.append(context.D)

import csv
@then(u'He Make CSV File Of Those')
def Saving_Information_To_CSv(context):

    field_names = ['name', 'rating', 'address', 'review', 'Log_and_Lat']
    with open('details.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list(context.D.keys()))
        writer.writeheader()
        writer.writerows(context.details)