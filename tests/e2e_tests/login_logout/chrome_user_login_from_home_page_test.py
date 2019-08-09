import allure
from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from expected_results.users.jane_doe import JaneDoe
from page_models.home_page_model import HomePageModel
from utils.http_status_code import get_http_status_code
from selenium.common.exceptions import NoSuchElementException
from tests.context_cases.home_page_context_case import HomePageContextCase
from expected_results.page_context.home_page_context import HomePageContext
from expected_results.page_context.bank_account_context import BankAccountContext


@allure.suite("Chrome Browser")
@allure.sub_suite('User Login/Logout')
@allure.feature("Home Page")
@screenshot_on_fail()
class TestChromeUserLoginFromHomePage(HomePageContextCase):

	@classmethod
	def setUpClass(cls):
		with allure.step("Open web browser"):
			cls.user = JaneDoe
			cls.browser = 'chrome'
			cls.page_model = HomePageModel
			cls.page_context = HomePageContext
			get_http_status_code(HomePageContext.URL)
			cls.page = open_web_browser(browser=cls.browser,
			                            page_model=cls.page_model,
			                            page_context=cls.page_context)

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close web browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	def test_user_login_logout(self):
		allure.dynamic.description("""
				User log in validation > Login from Home page:
					1. Open Home web page
					2. Do URL verification
					3. Do Title verification
					4. Type username/password
					5. Hit "Log In" button
					6. Verify "Welcome" message
					7. Do URL verification
					8. Log Out
					9. Do URL verification
					10. Verify that "Account Services" menu is not displayed
					11. Verify web page title
					12. Close web browser
				""")
		allure.dynamic.title("Web page URL test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# test url
		self.verify_page_url()

		# Verify Page Title
		self.verify_page_title()

		with allure.step('Type Username'):
			expected = self.user.USERNAME
			self.page.enter_username(expected)

			with allure.step('Verify Username value'):
				actual = self.page.username
				print('\nStep: {}\nExpected: {}\nActual: {}'.format('Verify Username value',
				                                                    expected,
				                                                    actual))
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))

		with allure.step('Type Password'):
			expected = self.user.PASSWORD
			self.page.enter_password(expected)

			with allure.step('Verify Password value'):
				actual = self.page.password
				print('\nStep: {}\nExpected: {}\nActual: {}'.format('Verify Password value',
				                                                    expected,
				                                                    actual))
				self.assertEqual(expected,
				                 actual,
				                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
				                                                                                    actual))

		with allure.step('Hit Log In button'):
			self.page.hit_login_button()

		# Verify "Welcome" message
		with allure.step('Verify "Welcome" message'):
			expected = '{}{} {}'.format(BankAccountContext.ACCOUNT_SERVICES_MENU['welcome_message'],
			                            self.user.FIRST_NAME,
			                            self.user.LAST_NAME)
			actual = self.page.welcome_message
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('Verify "Welcome" message',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))

		# Log Out
		with allure.step('Hit "Log Out" link'):
			self.page.log_out()

		# Post Logout validation
		with allure.step('Do URL verification'):
			expected = 'https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC'
			actual = self.page.url
			print('\nStep: {}\nExpected: {}\nActual: {}'.format('\'Verify URL\'',
			                                                    expected,
			                                                    actual))
			self.assertEqual(expected,
			                 actual,
			                 msg="Expected <{}> value does not equal actual <{}> result".format(expected,
			                                                                                    actual))
		# TODO: Fix this one
		'''
		with allure.step('Verify that "Account Services" menu is not displayed'):
			with self.assertRaises(NoSuchElementException):
				title = self.page.menu_title
		'''

		# Verify Page Title
		self.verify_page_title()