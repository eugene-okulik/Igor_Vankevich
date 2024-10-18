from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

first_name = 'Garold'
last_name = 'Kumar'
email = 'blabla@test.com'
gender = 'Male'
number = '1234567890'
subjects = 'mathematics'
hobbies = 'Music'
address = 'velokochanya 13'
day = '23'
year = '1995'
month = 'March'
state = 'NCR'
city = 'Delhi'

driver = webdriver.Edge()
driver.maximize_window()
driver.get('https://demoqa.com/automation-practice-form')
first_name_string = driver.find_element(By.ID, 'firstName')
first_name_string.send_keys(first_name)
last_name_string = driver.find_element(By.ID, 'lastName')
last_name_string.send_keys(last_name)
email_string = driver.find_element(By.ID, 'userEmail')
email_string.send_keys(email)
male_radio = driver.find_element(By.XPATH, f"//label[contains(text(), '{gender}')]")
male_radio.click()
mobile_string = driver.find_element(By.ID, 'userNumber')
mobile_string.send_keys(number)
date_string = driver.find_element(By.CLASS_NAME, 'react-datepicker__input-container')
date_string.click()
month_birth = driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')
dropdown_month = Select(month_birth)
dropdown_month.select_by_visible_text(month)
year_birth = driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select')
dropdown_year = Select(year_birth)
dropdown_year.select_by_visible_text(year)
day_birth = driver.find_element(
    By.XPATH,
    f"//div[@class='react-datepicker__month']//div[contains(@class, 'react-datepicker__day') and text()='{day}']")
day_birth.click()
subjects_input = driver.find_element(By.ID, "subjectsInput")
subjects_input.click()
subjects_input.send_keys("Math")
subjects_input.send_keys(Keys.TAB)
hobbies_checkbox = driver.find_element(By.XPATH, f"//label[contains(text(), '{hobbies}')]")
hobbies_checkbox.click()
address_form = driver.find_element(By.ID, 'currentAddress')
address_form.send_keys(address)
state_dropdown = driver.find_element(By.ID, 'state')
state_dropdown.click()
state_select = driver.find_element(By.XPATH, f"//div[text()='{state}']")
state_select.click()
city_dropdown = driver.find_element(By.ID, 'city')
city_dropdown.click()
city_select = driver.find_element(By.XPATH, f"//div[text()='{city}']")
city_select.click()
submit = driver.find_element(By.ID, 'submit')
submit.click()
info_window = driver.find_element(By.CLASS_NAME, 'modal-body')
print(info_window.text)
