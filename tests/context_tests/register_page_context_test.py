#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure

from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from utils.browser_configuration import browser_configuration

from page_models.register_page_model import RegisterPageModel
from expected_results.page_context.register_page_context import RegisterPageContext
from tests.context_tests.context_cases.register_page_context_case import RegisterPageContextCase


@allure.suite("Chrome Browser Context Testing")
@allure.sub_suite('Chrome Register Page Context Test')
@allure.feature("Register Page")
@screenshot_on_fail()
class TestChromeRegisterPageContext(RegisterPageContextCase):

	@classmethod
	def setUpClass(cls):
		with allure.step("Open web browser"):
			cls.browser = browser_configuration()
			cls.page_model = RegisterPageModel
			cls.page_context = RegisterPageContext
			cls.page = open_web_browser(browser=cls.browser,
			                            page_model=cls.page_model,
			                            page_context=cls.page_context)

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
		Context base elements validation > Register page title:
			1. Open Register page web page
			2. Do Register page title verification
		""")
		allure.dynamic.title("Register page title test")
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Verify web page title
		self.verify_page_title()

	# Registration page context - Personal Info Context base elements validation
	def test_first_name_title(self):
		allure.dynamic.description("""
		Context base elements validation > Register Form:
			1. Open Register web page
			2. Do First Name title verification
		""")
		allure.dynamic.title("First Name title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Context base elements validation:
		self.verify_first_name_title()

	@allure.feature("Base Personal Info Context")
	def test_last_name_title(self):
		allure.dynamic.description("""
		Context base elements validation > Register Form:
			1. Open Register web page
			2. Do Last Name title verification
		""")
		allure.dynamic.title("Last Name title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Context base elements validation:
		self.verify_last_name_title()

	@allure.feature("Base Personal Info Context")
	def test_address_title(self):
		allure.dynamic.description("""
		Context base elements validation > Register Form:
			1. Open Register web page
			2. Do Address title verification
		""")
		allure.dynamic.title("Address title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Context base elements validation:
		self.verify_address_title()

	@allure.feature("Base Personal Info Context")
	def test_city_title(self):
		allure.dynamic.description("""
		Context base elements validation > Register Form:
			1. Open Register web page
			2. Do City title verification
		""")
		allure.dynamic.title("City title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Context base elements validation:
		self.verify_city_title()

	@allure.feature("Base Personal Info Context")
	def test_state_title(self):
		allure.dynamic.description("""
		Context base elements validation > Register Form:
			1. Open Register web page
			2. Do State title verification
		""")
		allure.dynamic.title("State title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Context base elements validation:
		self.verify_state_title()

	@allure.feature("Base Personal Info Context")
	def test_zip_code_title(self):
		allure.dynamic.description("""
		Context base elements validation > Register Form:
			1. Open Register web page
			2. Do Zip Code title verification
		""")
		allure.dynamic.title("Zip Code title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Context base elements validation:
		self.verify_zip_code_title()

	@allure.feature("Base Personal Info Context")
	def test_phone_title(self):
		allure.dynamic.description("""
		Context base elements validation > Register Form:
			1. Open Register web page
			2. Do Phone title verification
		""")
		allure.dynamic.title("Phone title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Context base elements validation:
		self.verify_phone_title()

	@allure.feature("Base Personal Info Context")
	def test_ssn_title(self):
		allure.dynamic.description("""
		Context base elements validation > Register Form:
			1. Open Register web page
			2. Do SSN title verification
		""")
		allure.dynamic.title("SSN title test")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		# Personal Info Context base elements validation:
		self.verify_ssn_title()

	# Registration page context - Register web page context base elements validation
	@allure.feature("Register Page")
	def test_username_title(self):
		allure.dynamic.description("""
		Context base elements validation > Register Form:
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
		Context base elements validation > Register Form:
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
		Context base elements validation > Register Form:
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
		Context base elements validation > Register Form:
			1. Open Register web page
			2. Do "Register" button verification
		""")
		allure.dynamic.title("\"Register\" button test")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		# Register web page elements validation:
		self.verify_register_button()