import pytest

sale_text = 'Sale'
title_text = 'Women Sale'
sale_off_text = 'Every $200-plus purchase!'


@pytest.mark.smoke
def test_title_page(sale_page):
    sale_page.open_page()
    sale_page.page_title(sale_text)


@pytest.mark.button_to_women_sale
def test_transition_to_woman_sale(sale_page):
    sale_page.open_page()
    sale_page.transition_to_woman_sale(title_text)


@pytest.mark.sale_off
def test_text_sale_off(sale_page):
    sale_page.open_page()
    sale_page.sale_off(sale_off_text)
