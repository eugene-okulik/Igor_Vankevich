import pytest

fname = 'Ryan'
lname = 'Gosling'
email = 'r112lgtrhrefwefe@gmail.com'
passwd = 'fkewhfukfhue2131JIJIH'
confpasswd = 'fkewhfukfhue2131JIJIH'
min_len_passwd = '1'
len_text_passwd = (
    'Minimum length of this field must be equal or greater than 8 symbols. '
    'Leading and trailing spaces will be ignored.'
)
similar_characters_password = '11111111'
similar_text = (
    'Minimum of different classes of characters in password is 3. '
    'Classes of characters: Lower Case, Upper Case, Digits, Special Characters.'
)
message_empty_field = 'This is a required field.'


@pytest.mark.smoke
def test_create_akk(registration_page):
    registration_page.open_page()
    registration_page.fill_create_akk_form(fname,
                                           lname,
                                           email,
                                           passwd,
                                           confpasswd
                                           )
    registration_page.data_verification(fname, lname, email)


@pytest.mark.rules_passwd
def test_message_rules_passwd(registration_page):
    registration_page.open_page()
    registration_page.rules_passwd(min_len_passwd, len_text_passwd)
    registration_page.rules_passwd(similar_characters_password, similar_text)


@pytest.mark.message_empty_field
def test_create_akk_with_empty_fields(registration_page):
    registration_page.open_page()
    registration_page.create_with_empty_field(message_empty_field)
