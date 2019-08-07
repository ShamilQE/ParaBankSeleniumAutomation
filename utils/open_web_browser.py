import allure
from utils.driver import Driver
from utils.refresh_page import refresh_page


def open_web_browser(browser: str, page_model, page_context):

	# Open web page
	with allure.step("Open web browser on {}.".format(page_context.URL)):
		driver = Driver(browser)
		page = page_model(driver=driver, implicit_wait_time=5, explicit_wait_time=10)
		page.go()
		refresh_page(page_context.TITLE, page)
		return page