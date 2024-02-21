Feature: Indra Avitech Assignment

 # Negative scenario
  Scenario: Login with invalid credentials
	Given the user is on the login page
	When the user enters email "invaliduser@gmail.com" and password "InvalidPassword"
	And the user clicks the login button
	Then the user should see an error message

 # Positive scenario
  Scenario Outline: Successful login and logout
	Given the user is on the login page
	When the user enters email "<email>" and password "********"
	And the user clicks the login button
	Then the user should be redirected to the inbox page
	When the user clicks the logout button
	Then the user should be redirected to the login page

	Examples:
	  | email   |
	  | indraavitech_1@lvconsult.sk |
