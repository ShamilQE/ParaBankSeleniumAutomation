import allure
from utils.driver import Driver
from utils.screenshot import screenshot_on_fail
from page_models.about_page_model import AboutPageModel
from tests.context_tests.base_context_case import TestBaseContextCase
from expected_results.page_context.about_page_context import AboutPageContext


@allure.feature("About Page")
@allure.story('About Context')
@allure.suite('About Page Context Test Suite')
@screenshot_on_fail()
class AboutPageContextTestCase(TestBaseContextCase):

	def open_web_browser(self, browser):
		# Open web page
		with allure.step("Open web browser on: {}".format(AboutPageContext.URL)):
			driver = Driver(browser)
			self.page = AboutPageModel(driver=driver, implicit_wait_time=5, explicit_wait_time=10)
			self.page.go()

	@allure.feature("About Page")
	def verify_page_url(self):
		with allure.step("About page URL test"):
			self.assertEqual(AboutPageContext.URL,
			                 self.page.url)

	@allure.feature("About Page")
	def verify_page_title(self):
		with allure.step("About page title test"):
			self.assertEqual(AboutPageContext.TITLE,
			                 self.page.title)

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

	@allure.feature("About Page")
	def verify_description_title(self):
		# Context About page elements validation:
		with allure.step("Description title test"):
			self.assertEqual(AboutPageContext.DESCRIPTION['title'], self.page.description_title)

	@allure.feature("About Page")
	def verify_description_text(self):
		# Context About page elements validation:
		with allure.step("Description text (first paragraph) test"):
			self.assertEqual(AboutPageContext.DESCRIPTION['text'][0], self.page.description_first_line)

		with allure.step("Description text (second paragraph) test"):
			self.assertEqual(AboutPageContext.DESCRIPTION['text'][1], self.page.description_second_line)

		with allure.step("Description text (third paragraph) test"):
			self.assertEqual(AboutPageContext.DESCRIPTION['text'][2], self.page.description_third_line)

		with allure.step("Description text (fourth paragraph) test"):
			self.assertEqual(AboutPageContext.LINK, self.page.description_link)
