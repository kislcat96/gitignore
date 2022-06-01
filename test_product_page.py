import time
import pytest
from login_page import LoginPage
from product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException

# @pytest.mark.new_user
# class TestUserAddToBasketFromProductPage():
#     @pytest.fixture(autouse=True)
#     def setup(self, browser):
#         linka = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#         email = str(time.time()) + "@fakemail.org"
#         password = "426244123ABCdefhg"
#         product_page = ProductPage(browser, linka)
#         product_page.open()
#         product_page.go_to_login_page()
#         page = LoginPage(browser, browser.current_url)
#         page.open()
#         page.register_new_user(email, password)
#         page.should_be_authorized_user()


def test_guest_can_add_product_to_basket(self, browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.product_name_is_correct()
    page.should_be_correct_adding_product_price()


def test_guest_cant_see_success_message_after_adding_product_to_baske(self, browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
