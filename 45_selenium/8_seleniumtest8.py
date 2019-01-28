"""
Demo of working with Checkboxes using Selenium Webdriver
"""

from selenium import webdriver


driver = webdriver.Chrome()

#save the url to navigate to
url = 'https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_radio'

#Navigate to the url
driver.get(url)

def assert_element_is_checkbox(element):
    """
    Function to check a passed in element is a html checkbox element.
    Raises an assertion exception if the element is not a checkbox.
    :param element: the element object to be checked
    """

    my_element_type = element.get_attribute('type')

    if my_element_type != 'checkbox':
        raise AssertionError('The passed is not a checkbox')

    return

def is_checkbox_selected(element):
    """
    Function to check if a checkbox is checked or not.
    It will return 'True' if checked or 'False' if not checked.
    :param element:
    :return: boolean
    """

    assert_element_is_checkbox(element)

    if element.is_selected():
        return True
    else:
        return False

def assert_checkbox_is_selected(element):
    """
    Function to assert if a check box is select.
    Will raise an assertion exception if the passed in element is not a check box or it is not checked.
    :param element:
    :return:
    """
    assert_element_is_checkbox(element)

    if not is_checkbox_selected(element):
        raise  AssertionError('The element is not selected.')

    return

def assert_checkbox_is_enabled(element):
    """
    Function to verify if the passed in element is enabled. Enabled element is clickable/selectable.
    Raises an assertion exception if the element is not checkbox or is not enabled.
    :param element:
    :return:
    """
    assert_element_is_checkbox(element)

    if not element.is_enabled():
        raise  AssertionError('The checkbox is not enabled.')


# Start of function calls

java_box = driver.find_element_by_name('java')

print(is_checkbox_selected(java_box))
assert_checkbox_is_enabled(java_box)

php_box = driver.find_element_by_name('php')
print(php_box.is_enabled())
