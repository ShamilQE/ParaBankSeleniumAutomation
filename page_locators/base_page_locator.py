from selenium.webdriver.common.by import By


class BasePageLocator:
	'''
	Holds all relevant locators for any page web elements.
	Each locator is a tuple.
	Separate the locator strings from the place where they are being used.
	'''

	SLOGAN = (By.XPATH, '//*[@id="topPanel"]/p')
	ADMIN_LOGO_HREF = (By.CSS_SELECTOR, 'div[id="topPanel"] > a[href="/parabank/admin.htm"]')
	ADMIN_LOGO_IMG = (By.XPATH, '//*[@id="topPanel"]/a[1]/img')
