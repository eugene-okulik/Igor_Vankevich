from Igor_Vankevich.test_UI_PW_Igor_Vankevich.pages.base_page import BasePage
from Igor_Vankevich.test_UI_PW_Igor_Vankevich.pages.locators import sale_locator as loc
from playwright.sync_api import expect


class SalePage(BasePage):
    page_url = '/sale.html'

    def page_title(self, text):
        title = self.find(loc.title_page_loc)
        expect(title.inner_text()).to_have_text(text)

    def transition_to_woman_sale(self, text):
        self.find(loc.woman_deals_button_loc).click()
        title_page = self.find(loc.title_page_loc)
        expect(title_page.inner_text()).to_have_text(text)

    def sale_off(self, text):
        sale_text = self.find(loc.sale_off_loc)
        expect(sale_text.inner_text()).to_have_text(text)
