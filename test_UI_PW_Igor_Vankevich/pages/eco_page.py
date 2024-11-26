from Igor_Vankevich.test_UI_PW_Igor_Vankevich.pages.base_page import BasePage
from Igor_Vankevich.test_UI_PW_Igor_Vankevich.pages.locators import eco_locator as loc
from playwright.sync_api import expect


class EcoPage(BasePage):
    page_url = '/collections/eco-friendly.html'
    item_return = None
    sort_first_item = None

    def adding_first_product_to_cart(self):
        item = self.find(loc.product_item_loc).hover()
        self.find(loc.product_size_loc).click()
        self.find(loc.product_color_loc).click()
        self.find(loc.button_add_cart_loc).click()
        self.item_return = item.text

    def check_name_item_in_page_message(self):
        page_message = self.find(loc.page_message_loc)
        assert self.item_return in page_message.text

    def check_adding_item_in_cart(self):
        self.find(loc.cart_button_loc).click()
        item_in_cart = self.find(loc.item_in_cart_loc)
        assert self.item_return == item_in_cart.text

    def switching_pages(self):
        current_url = self.page.url
        self.find(loc.switch_gape_loc).click()
        new_url = self.page.url
        assert new_url != current_url

    def sort_item(self, sort_by):
        self.find(loc.sorted_items_loc).click()
        self.find(sort_by).click()
        self.sort_first_item = self.find(loc.price_item).get_attribute('data-price-amount')

    def check_valid_sorted(self):
        self.find(loc.action_sorted).click()
        new_price_first_item = self.find(loc.new_price_item).get_attribute('data-price-amount')
        expect(self.sort_first_item < new_price_first_item)
