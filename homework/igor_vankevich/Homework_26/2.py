from playwright.sync_api import Page

fname = 'awdaw'
lname = 'adwadaw'
email = 'dwadedw@gmail.com'
mobile_num = '12312432334'
date_birth = '1 Nov 1994'
subjects = ["Math", "English", "Physics"]
state = 'NCR'
city = 'Delhi'
address = 'test test test'
gender_box = 'male'
hobbie_box = 'music'


def select_gender(page, gender):
    gender_locator = {
        "male": "label[for='gender-radio-1']",
        "female": "label[for='gender-radio-2']",
        "other": "label[for='gender-radio-3']"
    }

    if gender in gender_locator:
        page.click(gender_locator[gender])
    else:
        raise ValueError("Неверный пол. Доступные варианты: 'male', 'female', 'other'.")


def fill_subjects(page, subjects):
    for subject in subjects:
        page.fill("input#subjectsInput", subject)
        page.press("input#subjectsInput", "Enter")


def select_hobbies(page, hobbie):
    hobbies_locator = {
        "sports": "label[for='hobbies-checkbox-1']",
        "reading": "label[for='hobbies-checkbox-2']",
        "music": "label[for='hobbies-checkbox-3']"
    }

    if hobbie in hobbies_locator:
        page.click(hobbies_locator[hobbie])
    else:
        raise ValueError


def fill_form(page: Page):

    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill(fname)
    page.get_by_placeholder('Last Name').fill(lname)
    page.get_by_placeholder('name@example.com').fill(email)
    select_gender(page, gender_box)
    page.get_by_placeholder('Mobile Number').fill(mobile_num)
    page.fill("input#dateOfBirthInput", date_birth)
    fill_subjects(page, subjects)
    select_hobbies(page, hobbie_box)
    page.get_by_placeholder('Current Address').fill(address)
    page.get_by_text('Select State').click()
    page.fill("input#react-select-3-input", state)
    page.press("input#react-select-3-input", "Enter")
    page.get_by_text('Select City').click()
    page.fill("input#react-select-4-input", city)
    page.press("input#react-select-4-input", "Enter")
    page.get_by_role('button', name='Submit').click()
