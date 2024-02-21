import re
from playwright.sync_api import expect

class LoginPage:
	# Capture the web elements
	def __init__(self, page):
		self.page = page
		self.username_input = page.locator('[data-test="email-input"]')
		self.password_input = page.locator('[data-test="password-input"]')
		# self.login_btn = page.get_by_role("button", name="Prihlásiť")
		self.login_btn = page.query_selector('button[data-test="login-button"][type="submit"]')
		self.error_message = page.locator(".ws-state-banner")

	# Navigate to demo website
	def navigate(self):
		self.page.goto("https://mail.websupport.sk")

	# Type the credentials in login page
	def enter_credentials(self, email, password):
		self.username_input.fill(email)
		self.password_input.fill(password)

	# Click the login button
	def click_login_btn(self):
		self.login_btn.click()

	# Verify the login error message if occures.
	def verify_login_error(self):
		expect(self.error_message).to_be_visible()
		print("User can see an error message : " + self.error_message.inner_text())

	# Verify the login page title
	def verify_login_page_title(self):
		self.page.wait_for_timeout(2000) # wait 1 second
		expect(self.page).to_have_title(re.compile("Webmail Login | Websupport"))
		print("Login page after Logout has title : " + self.page.title())
