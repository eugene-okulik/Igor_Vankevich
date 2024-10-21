from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import pytest

product = 'Samsung galaxy s6'


@pytest.fixture()
def driver():
    edge_driver = webdriver.Edge()
    edge_driver.maximize_window()
    yield edge_driver


def test_add_to_cart(driver):
    driver.get("https://www.demoblaze.com/index.html")
    find_product = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, f'{product}'))
    )
    ActionChains(driver).key_down(Keys.CONTROL).click(find_product).key_up(Keys.CONTROL).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    add_to_cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Add to cart')]"))
    )
    add_to_cart.click()
    alert = Alert(driver)
    WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    cart = driver.find_element(By.ID, 'cartur')
    cart.click()
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="tbodyid"]/tr/td[2]'), f'{product}')
    )
    product_to_cart = driver.find_element(By.XPATH, '//*[@id="tbodyid"]/tr/td[2]')
    assert product_to_cart.text == product


def test_compare_product(driver):
    driver.get("https://magento.softwaretestingboard.com/gear/bags.html")
    actions = ActionChains(driver)
    first_product = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".product-item"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", first_product)
    actions.move_to_element(first_product).perform()
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="maincontent"]/div[3]/div[1]/div[3]/ol/li[1]/div/div/div[3]/div/div[1]/form/button')
        )
    )
    add_to_cart_button.click()
    compare_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, ".//div[contains(@class, 'product-item')]"))
    )
    compare_products = compare_section.find_elements(By.CSS_SELECTOR, ".product-item")
    assert len(compare_products) >= 0
