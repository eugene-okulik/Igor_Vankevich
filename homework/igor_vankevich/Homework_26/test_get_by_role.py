from playwright.sync_api import Page, expect

user_name = 'asdffg'
password = 'qazwsx'


def test_authorization(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    link_auth = page.get_by_role('link', name='Form Authentication')
    link_auth.click()
    user_name_box = page.get_by_role('textbox', name='username')
    user_name_box.fill(user_name)
    passwd_box = page.get_by_role('textbox', name='password')
    passwd_box.fill(password)
    page.get_by_role('button').click()
    expect(page).to_have_url('https://the-internet.herokuapp.com/login')
