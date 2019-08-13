#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from utils.browser_configuration import browser_configuration

from page_object_models.register_page_model import RegisterPageModel
from expected_results.page_content.register_page_content import RegisterPageContent
from tests.content_tests.content_cases.register_page_content_case import RegisterPageContentCase


@allure.epic('Page Content')
@allure.parent_suite('Page Unique Content')
@allure.suite('Register Page Content')
@allure.sub_suite("Register Page Unique Content")
@allure.feature("Register Page")
@allure.story('Register Content')
@screenshot_on_fail()
class TestRegisterPageContent(RegisterPageContentCase):

	@classmethod
	def setUpClass(cls):
		with allure.step("Open web browser"):
			cls.browser = browser_configuration()
			cls.page_model = RegisterPageModel
			cls.page_content = RegisterPageContent
			cls.page = open_web_browser(browser=cls.browser,
			                            page_model=cls.page_model,
			                            page_content=cls.page_content)

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close web browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	# Generic/Base context
	def test_page_url(self):
		allure.dynamic.description("""
		ontext base elements validation > Register page URL:
			1. Open Register page web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page URL test")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		# Verify web page url
		self.verify_page_url()

	def test_page_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register page title:
			1. Open Register page web page
			2. Do Register page title verification
		""")
		allure.dynamic.title("Register page title test")
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Verify web page title
		self.verify_page_title()

	# Registration page context - Personal Info Content base elements validation
	def test_first_name_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do First Name title verification
		""")
		allure.dynamic.title("First Name title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Content base elements validation:
		self.verify_first_name_title()

	@allure.feature("Base Personal Info Content")
	def test_last_name_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do Last Name title verification
		""")
		allure.dynamic.title("Last Name title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Content base elements validation:
		self.verify_last_name_title()

	@allure.feature("Base Personal Info Content")
	def test_address_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do Address title verification
		""")
		allure.dynamic.title("Address title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Content base elements validation:
		self.verify_address_title()

	@allure.feature("Base Personal Info Content")
	def test_city_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do City title verification
		""")
		allure.dynamic.title("City title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Content base elements validation:
		self.verify_city_title()

	@allure.feature("Base Personal Info Content")
	def test_state_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do State title verification
		""")
		allure.dynamic.title("State title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Content base elements validation:
		self.verify_state_title()

	@allure.feature("Base Personal Info Content")
	def test_zip_code_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do Zip Code title verification
		""")
		allure.dynamic.title("Zip Code title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Content base elements validation:
		self.verify_zip_code_title()

	@allure.feature("Base Personal Info Content")
	def test_phone_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do Phone title verification
		""")
		allure.dynamic.title("Phone title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Content base elements validation:
		self.verify_phone_title()

	@allure.feature("Base Personal Info Content")
	def test_ssn_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do SSN title verification
		""")
		allure.dynamic.title("SSN title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Content base elements validation:
		self.verify_ssn_title()

	# Registration page context - Register web page context base elements validation
	@allure.feature("Register Page")
	def test_username_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do Username title verification
		""")
		allure.dynamic.title("Username title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Register web page elements validation:
		self.verify_username_title()

	@allure.feature("Register Page")
	def test_password_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do Password title verification
		""")
		allure.dynamic.title("Password title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Register web page elements validation:
		self.verify_password_title()

	@allure.feature("Register Page")
	def test_confirm_title(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do Confirm title verification
		""")
		allure.dynamic.title("Confirm title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Register web page elements validation:
		self.verify_confirm_title()

	@allure.feature("Register Page")
	def test_register_button(self):
		allure.dynamic.description("""
		Content base elements validation > Register Form:
			1. Open Register web page
			2. Do "Register" button verification
		""")
		allure.dynamic.title("\"Register\" button test")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		# Register web page elements validation:
		self.verify_register_button()
