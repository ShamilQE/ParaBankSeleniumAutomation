#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from tests.config import Config
from utils.clean_database import clean_database
from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser

from expected_results.users.base_user import BaseUser
from expected_results.users.invalid_users_templates.no_such_user import NoSuchUser
from expected_results.page_content.forgot_login_info_page_content import ForgotLoginInfoPageContent

from tests.e2e_tests.base_case.user_personal_info_case import UserPersonalInfoCase
from page_object_models.forgot_login_info_page_model import ForgotLoginInfoPageModel
from utils.step_definition import step_definition


@allure.epic('Page Functionality')
@allure.parent_suite('End To End')
@allure.suite("Forgot Login")
@allure.sub_suite('Negative Tests')
@allure.feature("Forgot Login Page")
@allure.story('Forgot Login Functionality')
@screenshot_on_fail()
class TestForgotLoginAllFieldsEmpty(UserPersonalInfoCase):

	@classmethod
	def setUpClass(cls):
		cls.client = BaseUser(NoSuchUser)
		cls.page = None
		cls.config = Config()

		with allure.step("Initial data setup > clean DB"):
			clean_database(cls.config)

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close Web Browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	def setUp(self):
		with allure.step("Initial data setup: {}".format(ForgotLoginInfoPageContent.URL)):
			self.page_model = ForgotLoginInfoPageModel
			self.page_context = ForgotLoginInfoPageContent
			with allure.step("Open web browser"):
				self.page = open_web_browser(config=self.config,
				                             page_model=self.page_model,
				                             page_content=self.page_context)

	def tearDown(self):
		with allure.step("Close current tab"):
			if self.page:
				self.page.close()

	def test_user_registration(self):
		allure.dynamic.description("""
		Forgot Login Info test case:
			1. Open 'Forgot Login Info' web page
			2. Fill out user personal data > Set all fields empty
			3. Verify that each data item (No such user) appears in relevant field
			4. Hit 'FIND MY LOGIN' button
			5. Verify 'Error' message
			6. Verify Error title
			7. Close web browser
		""")
		allure.dynamic.title("User registration > Negative test > No such user")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		# Register a new user:
		self.fill_out_user_data()

		with allure.step('Hit "FIND MY LOGIN INFO" button'):
			print('Hit "FIND MY LOGIN INFO" button')
			self.page.hit_find_info_btn()

		step_definition(self,
		                step_description="Verify Error title",
		                expected=ForgotLoginInfoPageContent.ERROR_TITLE,
		                actual=self.page.error_title,
		                act=None,
		                click=False)

		step_definition(self,
		                step_description="Verify Error message",
		                expected=ForgotLoginInfoPageContent.ERROR_MESSAGE,
		                actual=self.page.error_message,
		                act=None,
		                click=False)

