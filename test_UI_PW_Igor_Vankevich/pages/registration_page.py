from Igor_Vankevich.test_UI_PW_Igor_Vankevich.pages.base_page import BasePage
from Igor_Vankevich.test_UI_PW_Igor_Vankevich.pages.locators import registration_locator as loc
from playwright.sync_api import expect


class RegistrationPage(BasePage):
    page_url = '/customer/account/create/'

    def fill_create_akk_form(self,
                             fname,
                             lname,
                             email,
                             passwd,
                             confpasswd
                             ):
        name_field = self.find(loc.fname_field_loc)
        lname_field = self.find(loc.lname_field_loc)
        email_field = self.find(loc.email_field_loc)
        password_field = self.find(loc.pass_field_loc)
        conf_password_field = self.find(loc.confirm_pass_field_loc)
        name_field.fill(fname)
        lname_field.fill(lname)
        email_field.fill(email)
        password_field.fill(passwd)
        conf_password_field.fill(confpasswd)
        self.find(loc.create_button_loc).click()
        page_message = self.find(loc.page_message_loc)
        expect(page_message.inner_text()).to_have_text('Thank you for registering with Main Website Store.')

    def data_verification(self, fname, lname, email):
        info_akk = self.find(loc.info_loc)
        expect(info_akk).to_have_text(fname, lname, email)

    def rules_passwd(self, passwd, text):
        invalid_passwd = self.find(loc.pass_field_loc)
        invalid_passwd.fill(passwd)
        err_passwd = self.find(loc.password_error_loc)
        expect(err_passwd).to_have_text(text)

    def create_with_empty_field(self, text):
        self.find(loc.create_button_loc).click()
        err_empty_field = self.find(loc.err_empty_field_fname)
        expect(err_empty_field).to_have_text(text)
