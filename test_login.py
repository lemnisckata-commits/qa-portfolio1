from playwright.sync_api import sync_playwright
import pytest

def get_page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    return playwright, browser, page

def test_successful_login():
    playwright, browser, page = get_page()
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    assert page.url == "https://www.saucedemo.com/inventory.html"
    browser.close()
    playwright.stop()

def test_wrong_password():
    playwright, browser, page = get_page()
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "wrong_password")
    page.click("#login-button")
    assert page.locator(".error-message-container").is_visible()
    browser.close()
    playwright.stop()

def test_empty_fields():
    playwright, browser, page = get_page()
    page.goto("https://www.saucedemo.com")
    page.click("#login-button")
    assert page.locator(".error-message-container").is_visible()
    browser.close()
    playwright.stop()

def test_locked_user():
    playwright, browser, page = get_page()
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "locked_out_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    assert page.locator(".error-message-container").is_visible()
    browser.close()
    playwright.stop()