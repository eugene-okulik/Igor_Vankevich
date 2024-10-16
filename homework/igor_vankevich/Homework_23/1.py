from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get('https://www.qa-practice.com/elements/input/simple')
text_string = driver.find_element(By.ID, 'id_text_string')
text_string.send_keys('text_for_test')
text_string.submit()
input_text = driver.find_element(By.ID, 'result-text')
print(input_text.text)
