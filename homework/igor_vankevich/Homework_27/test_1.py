from playwright.sync_api import Page, Dialog, expect


def test_text_in_section(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/confirm')

    def accept_alert(alert: Dialog):
        alert.accept()

    page.on('dialog', accept_alert)
    page.get_by_role('link', name='Click').click()
    selected_text = page.locator('#result-text')
    expect(selected_text).to_have_text('Ok')
