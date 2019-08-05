import allure
from utils.driver import Driver
from utils.screenshot import screenshot_on_fail
from page_models.services_page_model import ServicesPageModel
from tests.context_tests.base_context_case import TestBaseContextCase
from expected_results.page_context.services_page_context import ServicesPageContext


@allure.feature("Services Page")
@allure.story('Services Context')
@allure.suite('Services Page Context Test Suite')
@screenshot_on_fail()
class ServicesPageContextTestCase(TestBaseContextCase):

	def open_web_browser(self, browser):
		with allure.step('Open web browser on: {}'.format(ServicesPageContext.URL)):
			# Open web page
			driver = Driver(browser)
			self.page = ServicesPageModel(driver=driver, implicit_wait_time=5, explicit_wait_time=10)
			self.page.go()

	@allure.feature("Services Page")
	def verify_page_url(self):

		allure.dynamic.severity(allure.severity_level.BLOCKER)
		with allure.step('Verify "Services" web page URL. Expected result: {}'.format(ServicesPageContext.URL)):
			self.assertEqual(ServicesPageContext.URL,
			                 self.page.url)

	@allure.feature("Services Page")
	def verify_page_title(self):
		allure.dynamic.severity(allure.severity_level.MINOR)
		with allure.step('Verify "Services" web page title. Expected result: {}'.format(ServicesPageContext.TITLE)):
			self.assertEqual(ServicesPageContext.TITLE,
			                 self.page.title)

	def verify_parabank_admin_logo(self):
		# Context base elements validation:
		self.parabank_admin_logo_test()

	def verify_parabank_logo(self):
		# Context base elements validation:
		self.parabank_logo_test()

	def verify_right_menu_home_button(self):
		# Context base elements validation:
		self.right_menu_home_button_test()

	def verify_right_menu_contact_button(self):
		# Context base elements validation:
		self.right_menu_contact_button_test()

	def verify_right_menu_about_button(self):
		# Context base elements validation:
		self.right_menu_about_button_test()

	def verify_solutions_menu_items(self):
		# Context base elements validation:
		self.solutions_menu_items_test()

	def verify_customer_login(self):
		# Context base elements validation:
		self.customer_login_test()

	def verify_footer_items(self):
		# Context base elements validation:
		self.footer_items_test()
