import pytest
from pages.registration_page import RegistrationPage
from pages.eco_page import EcoPage
from pages.sale_page import SalePage


@pytest.fixture()
def registration_page(page):
    return RegistrationPage(page)


@pytest.fixture()
def eco_page(page):
    return EcoPage(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)
