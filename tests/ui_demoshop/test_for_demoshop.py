import os

import allure
from dotenv import load_dotenv
from selene import have

load_dotenv()


def test_login_with_api(browser_open):
    browser_open.open("")

    with allure.step("Verify successful authorization"):
        browser_open.element(".account").should(have.text(os.getenv("LOGIN")))


def test_search_negative_result(browser_open):
    browser_open.open("")

    with allure.step("Negitive search"):
        browser_open.element('.search-box [value="Search store"]').click()
        browser_open.element('.search-box [value="Search store"]').type('negative test').press_enter()
        browser_open.element('.result').should(have.text('No products were found that matched your criteria.'))


def test_watch_profile(browser_open):
    browser_open.open("")

    with allure.step("Check info in profile"):
        browser_open.element(".account").should(have.text(os.getenv('LOGIN'))).click()
        browser_open.element('#FirstName').should(have.value('mkdv'))
        browser_open.element('#LastName').should(have.value('00'))
        browser_open.element('#Email').should(have.value(os.getenv('LOGIN')))
        browser_open.element('[checked="checked"]#gender-male')


def test_watch_page_change_password(browser_open):
    browser_open.open("")

    with allure.step("Check text buttion in change password"):
        browser_open.element(".account").should(have.text(os.getenv('LOGIN'))).click()
        browser_open.element('[href="/customer/changepassword"]').should(have.text('Change password')).click()
        browser_open.element('[for="OldPassword"]').should(have.text('Old password:'))
        browser_open.element('[for="NewPassword"]').should(have.text('New password:'))
        browser_open.element('[for="ConfirmNewPassword"]').should(have.text('Confirm password:'))


def test_logout(browser_open):
    browser_open.open("")

    with allure.step("Check logout"):
        browser_open.element('.ico-logout').click()
        browser_open.element('.ico-login').should(have.text('Log in'))