from pages.main_page import MainPage
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"


def go_to_login_page(browser):
    link = browser.find_element_by_css_selector("#login_link")
    link.click()


time.sleep(30)


def test_add_to_cart(browser):
    page = page(link, browser)   # инициализируем объект Page Object
    page.open()                           # открываем страницу в браузере
    # проверяем что есть кнопка добавления в корзину
    page.should_be_add_to_cart_button()
    page.add_product_to_cart()            # жмем кнопку добавить в корзину
    page.should_be_success_message()  # проверяем что есть сообщение с нужным текстом


time.sleep(30)


def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)


time.sleep(30)
