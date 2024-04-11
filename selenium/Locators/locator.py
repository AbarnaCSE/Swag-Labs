from selenium.webdriver.common.by import By
class WebLocators:
   def __init__(self):
       self.usernameLocator = "user-name"
       self.passwordLocator = "password"
       self.buttonLocator = "login-button"
       self.menulocator = "react-burger-menu-btn"
       self.logoutlocator = "logout_sidebar_link"

   def enterText(self, driver, locator, textValue):
       driver.find_element(by=By.ID, value=locator).send_keys(textValue)


   def clickButton(self, driver, locator):
       driver.find_element(by=By.ID, value=locator).click()
