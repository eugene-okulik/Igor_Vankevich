from playwright.sync_api import Page, expect, BrowserContext


def test_button_with_new_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    new_page_button = page.get_by_role('link', name='Click')
    with context.expect_page() as new_page_event:
        new_page_button.click()
    new_page = new_page_event.value
    result = new_page.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    page_button = page.get_by_role('link', name='Click')
    expect(page_button).to_be_enabled()
