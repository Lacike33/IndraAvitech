import pytest
from pytest_bdd import given, when, then, scenarios, parsers, scenario
from pages.login_page import LoginPage
from pages.inbox_page import InboxPage
from playwright.sync_api import Page

scenarios('zadanie.feature')

#	***************		Help functions		**************

# Read the password from file
def get_password():
	with open("credentials.txt", "r") as file:
		return file.readline().strip()

#	***************		Step definitions		**************
@given("the user is on the login page")
def open_login_page(page: Page):
	login_page = LoginPage(page)
	login_page.navigate()

@when(parsers.parse('the user enters email "{email}" and password "{password}"'))
def enter_valid_credentials(page: Page, email, password):
	login_page = LoginPage(page)
	login_page.enter_credentials(email, get_password())

@when('the user clicks the login button')
def click_login_button(page: Page):
	login_page = LoginPage(page)
	login_page.click_login_btn()

@when('the user clicks the logout button')
def click_logout_button(page: Page):
	inbox_page = InboxPage(page)
	inbox_page.click_logout_btn()

@then('the user should see an error message')
def verify_error_message(page: Page):
	login_page = LoginPage(page)
	login_page.verify_login_error()

@then('the user should be redirected to the inbox page')
def verify_dashboard_redirect(page: Page):
	inbox_page = InboxPage(page)
	inbox_page.verify_inbox_page_title()

@then('the user should be redirected to the login page')
def verify_login_page_redirect(page: Page):
	login_page = LoginPage(page)
	login_page.verify_login_page_title()
