#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import unittest

from tests.config import Config
from utils.screenshot import screenshot_on_fail
from utils.open_web_browser import open_web_browser
from utils.step_definition import step_definition

from page_object_models.services_page_model import ServicesPageModel
from expected_results.page_content.services_page_content import ServicesPageContent


@allure.epic('Page Content')
@allure.parent_suite('Page Unique Content')
@allure.suite('Services Page Content')
@allure.sub_suite("Services Page Unique Content")
@allure.feature("Services Page")
@allure.story('Services Content')
@screenshot_on_fail()
class TestServicesPageContent(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		with allure.step("Open web browser"):
			cls.page_model = ServicesPageModel
			cls.page_content = ServicesPageContent
			cls.config = Config()
			cls.page = open_web_browser(config=cls.config,
			                            page_model=cls.page_model,
			                            page_content=cls.page_content)

	@classmethod
	def tearDownClass(cls):
		with allure.step("Close web browser"):
			if cls.page:
				cls.page.quit()
				cls.page = None

	def test_page_url(self):
		allure.dynamic.description("""
		Content base elements validation > Services page URL:
			1. Open Services web page
			2. Do URL verification
		""")
		allure.dynamic.title("Web page URL test")
		allure.dynamic.severity(allure.severity_level.BLOCKER)

		# Verify web page url
		step_definition(self,
		                expected=self.config.base_url + ServicesPageContent.URL,
		                actual=self.page.url,
		                step_description='Verify "Services" web page URL')

	def test_page_title(self):
		allure.dynamic.description("""
		Content base elements validation > Services page title:
			1. Open Services web page
			2. Do Services page title verification
		""")
		allure.dynamic.title("Services page title test")
		allure.dynamic.severity(allure.severity_level.MINOR)

		# Verify web page title
		step_definition(self,
		                expected=ServicesPageContent.TITLE,
		                actual=self.page.title,
		                step_description='Verify "Services" web page title',
		                act=None,
		                click=False)
		'''
		with allure.step('Verify "Services" web page title. Expected result: {}'.format(ServicesPageContent.TITLE)):
			self.assertEqual(ServicesPageContent.TITLE, self.page.title())
		'''

	# Services Content Testing

