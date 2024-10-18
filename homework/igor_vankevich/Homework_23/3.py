from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

language = 'Python'
expected_text = 'Hello World!'


@pytest.fixture()
def driver():
    edge_driver = webdriver.Edge()
    edge_driver.maximize_window()
    yield edge_driver


def test_choose_language(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select_language = driver.find_element(By.ID, 'id_choose_language')
    dropdown = Select(select_language)
    dropdown.select_by_visible_text(language)
    submit = driver.find_element(By.ID, 'submit-id-submit')
    submit.click()
    input_text = driver.find_element(By.ID, 'result-text')
    assert input_text.text == language


def test_hello_world(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_button = driver.find_element(By.XPATH, "//button[text()='Start']")
    start_button.click()
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'finish'), 'Hello World!')
    )
    finish_text = driver.find_element(By.ID, 'finish')
    assert finish_text.text == expected_text
