import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Задаем параметры браузера"):
        browser.config.window_width = 1400
        browser.config.window_height = 900

    with allure.step("Ищем репозиторий"):
        s(".header-search-button").click()
        s("#query-builder-test").send_keys("eroshenkoam/allure-example")
        s("#query-builder-test").submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 76"):
        s(by.partial_text("#76")).should(be.visible)


def test_decorator_steps():
    open_main_page()
    config_window()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_number("#76")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")

@allure.step("Задаем параметры браузера")
def config_window():
    browser.config.window_width = 1400
    browser.config.window_height = 900

@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    s(".header-search-button").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-example")
    s("#query-builder-test").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()
