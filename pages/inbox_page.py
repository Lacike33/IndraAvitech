import re
from playwright.sync_api import expect

class InboxPage:
	# Capture the web elements
	def __init__(self, page):
		self.page = page
		self.newMail_btn = page.locator("#rcmbtn104")
		self.contacts_btn = page.locator("#rcmbtn108")
		self.logout_btn = page.locator("#rcmbtn112")

	# Click the logout button
	def click_logout_btn(self):
		self.logout_btn.click()

	# Click the contacts button
	def click_contacts_btn(self):
		self.contacts_btn.click()

	# Click the newMail button
	def click_new_Mail_btn(self):
		self.newMail_btn.click()

	# Verify the inbox title
	def verify_inbox_page_title(self):
		self.page.wait_for_timeout(2000) # wait 1 second
		expect(self.page).to_have_title(re.compile("Websupport Webmail :: Doručená pošta"))
		print("Inbox page after Login has title : " + self.page.title())
