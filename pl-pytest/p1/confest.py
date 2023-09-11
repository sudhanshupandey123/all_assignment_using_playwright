from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.locator('https://www.saucedemo.com')

test_example(page)