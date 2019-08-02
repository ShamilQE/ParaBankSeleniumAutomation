from utils.driver import Driver
from utils.screenshot import screenshot_on_fail
from page_models.home_page_model import HomePageModel
from page_context.home_page_context import HomePageContext
from tests.context_tests.base_context_case import BaseTestCase


@screenshot_on_fail()
class HomePageContextTestCase(BaseTestCase):

	def open_web_browser(self, browser):

		# Open web page
		driver = Driver(browser)
		self.page = HomePageModel(driver=driver, implicit_wait_time=5, explicit_wait_time=10)
		self.page.go()

	def verify_page_url_title(self):

		self.assertEqual(HomePageContext.URL,
		                 self.page.url)
		self.assertEqual(HomePageContext.TITLE,
		                 self.page.title)

	def verify_atm_services_context(self):

		self.assertEqual(HomePageContext.ATM_SERVICES['title'],
		                 self.page.atm_title)
		self.assertEqual(HomePageContext.ATM_SERVICES['Withdraw Funds']['text'],
		                 self.page.atm_withdraw_funds_text)
		self.assertEqual(HomePageContext.ATM_SERVICES['Withdraw Funds']['href'],
		                 self.page.atm_withdraw_funds_formated_href)


	def verify_parabank_admin_logo(self):

		# Context base elements validation:
		self.parabank_admin_logo_test()

	def verify_parabank_logo(self):

		# Context base elements validation:
		self.parabank_logo_test()

	def verify_right_menu_buttons(self):

		# Context base elements validation:
		self.right_menu_buttons_test()

	def verify_solutions_menu_items(self):

		# Context base elements validation:
		self.solutions_menu_items_test()

	def verify_customer_login(self):

		# Context base elements validation:
		self.customer_login_test()

	def verify_footer_items(self):

		# Context base elements validation:
		self.footer_items_test()


