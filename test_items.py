import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_busket_button(browser):
    browser.get(link)
    time.sleep(30)
    try:
      button_add_to_basket = browser.find_element_by_css_selector("#add_to_basket_form>button")
    except (AttributeError, TypeError):
      raise AssertionError('Wrong css selector or busket not found!')