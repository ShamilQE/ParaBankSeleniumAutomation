import allure
from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from page_models.home_page_model import HomePageModel
from tests.context_tests.home_page_context_case import HomePageContextCase
from expected_results.page_context.home_page_context import HomePageContext


@allure.suite("Chrome Browser Context Testing")
@allure.sub_suite('Chrome Home Base Page Context Test')
@allure.feature("Base Page")
@screenshot_on_fail()
class TestChromeHomeBasePageContext(HomePageContextCase):

	@classmethod
	def setUpClass(cls):
		with allure.step("Open web browser"):
			cls.browser = 'chrome'
			cls.page_model = HomePageModel
			cls.page_context = HomePageContext
			cls.page = open_web_browser(browser=cls.browser,
			                            page_model=cls.page_model,
			                            page_context=cls.page_context)

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close web browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	@allure.feature("Home Page")
	def test_page_url(self):

		allure.dynamic.description("""
		Context base elements validation > Home page URL:
			1. Open Home web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page URL test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# open web browser
		# allure.step
		# self.open_web_browser()

		# test url
		expected_url = HomePageContext.URL
		allure.step
		self.verify_page_url(expected_url)

	@allure.feature("Home Page")
	def test_page_title(self):
		allure.dynamic.description("""
		Context base elements validation > Home page title:
			1. Open Home web page
			2. Do web page title verification
		""")
		allure.dynamic.title("Web page title test")

		# open web browser
		# self.open_web_browser()

		# Verify Page Title
		self.verify_page_title()

	# Base Page Context
	@allure.feature("Base Page")
	def test_parabank_admin_logo(self):
		allure.dynamic.description("""
		Context base elements validation > Admin logo:
			1. Open Home web page
			2. Do Admin logo verification
		""")
		allure.dynamic.title("Admin logo test")

		# open web browser
		# self.open_web_browser()

		# Context base elements validation:
		self.verify_parabank_admin_logo()

	@allure.feature("Base Page")
	def test_parabank_logo(self):
		allure.dynamic.description("""
		Context base elements validation > 'ParaBank' logo:
			1. Open Home web page
			2. Do Admin logo verification
		""")
		allure.dynamic.title("'ParaBank' logo test")

		# open web browser
		# self.open_web_browser()

		# Context base elements validation:
		self.verify_parabank_logo()

	@allure.feature("Base Page")
	def test_right_menu_home_button(self):
		allure.dynamic.description("""
		Context base elements validation > 'Home' button:
			1. Open Home web page
			2. Do 'Home' button (right menu) verification
		""")
		allure.dynamic.title("'Home' button (right menu) test")

		# open web browser
		# self.open_web_browser()

		# Context base elements validation:
		self.verify_right_menu_home_button()

	@allure.feature("Base Page")
	def test_right_menu_about_button(self):
		"""Context base elements validation > Home button:
		1. Open Home web page
		2. Do About button verification: href + text
		"""
		allure.dynamic.description("""
		Context base elements validation > 'About' button:
			1. Open Home web page
			2. Do 'About' button (right menu) verification
		""")
		allure.dynamic.title("'About' button (right menu) test")

		# open web browser
		# self.open_web_browser()

		# Context base elements validation:
		self.verify_right_menu_about_button()

	@allure.feature("Base Page")
	def test_right_menu_contact_button(self):
		allure.dynamic.description("""
		Context base elements validation > 'Contact' button:
			1. Open Home web page
			2. Do 'Contact' button (right menu) verification
		""")
		allure.dynamic.title("'Contact' button (right menu) test")

		# open web browser
		# self.open_web_browser()

		# Context base elements validation:
		self.verify_right_menu_contact_button()

	@allure.feature("Base Page")
	def test_solutions_menu_items(self):
		allure.dynamic.description("""
		Context base elements validation > 'Solutions' menu items:
			1. Open Home web page
			2. Do 'Solutions' menu items verification
		""")
		allure.dynamic.title("'Solutions' menu items test")

		# open web browser
		# self.open_web_browser()

		# Context base elements validation:
		self.verify_solutions_menu_items()

	@allure.feature("Base Page")
	def test_customer_login(self):
		allure.dynamic.description("""
		Context base elements validation > 'Customer Login':
			1. Open Home web page
			2. Do 'Customer Login' items verification
		""")
		allure.dynamic.title("'Customer Login' test")

		# open web browser
		# self.open_web_browser()

		# Context base elements validation:
		self.verify_customer_login()

	@allure.feature("Base Page")
	def test_footer_items(self):
		allure.dynamic.description("""
		Context base elements validation > 'Footer':
			1. Open Home web page
			2. Do 'Footer' items verification
		""")

		allure.dynamic.title("'Footer' test")

		# open web browser
		# self.open_web_browser()

		# Context base elements validation:
		self.verify_footer_items()

