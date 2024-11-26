import pytest
sort_by = 'price'


@pytest.mark.smoke
def test_adding_to_cart(eco_page):
    eco_page.open_page()
    eco_page.adding_first_product_to_cart()
    eco_page.check_name_item_in_page_message()
    eco_page.check_adding_item_in_cart()


@pytest.mark.switching_page
def test_switching_page(eco_page):
    eco_page.open_page()
    eco_page.switching_pages()


@pytest.mark.sorted_items
def test_sort_item(eco_page):
    eco_page.open_page()
    eco_page.sort_item(sort_by)
    eco_page.check_valid_sorted()
