from playwright.sync_api import Page, expect


def test_color_change(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    color_button = page.get_by_role('button', name='Color Change')
    page.wait_for_load_state(expect(color_button).to_have_css('color', 'rgb(220, 53, 69)'))
    color_button.click()