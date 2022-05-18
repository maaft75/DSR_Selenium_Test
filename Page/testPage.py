from selenium.webdriver.common.by import By
from DSRTest.Locators.locators import Locators


class testPage:
    def __init__(self, driver):
        self.driver = driver

    def inputAndClickFields(self, firstName, lastName, email, phoneNumber):
        self.driver.find_element(By.NAME, Locators.firstNameField).clear()
        self.driver.find_element(By.NAME, Locators.firstNameField).send_keys(firstName)
        self.driver.find_element(By.NAME, Locators.lastNameField).clear()
        self.driver.find_element(By.NAME, Locators.lastNameField).send_keys(lastName)
        self.driver.find_element(By.NAME, Locators.emailField).clear()
        self.driver.find_element(By.NAME, Locators.emailField).send_keys(email)
        self.driver.find_element(By.NAME, Locators.phoneNumberField).clear()
        self.driver.find_element(By.NAME, Locators.phoneNumberField).send_keys(phoneNumber)

    def clickOnMaleRadioButton(self):
        self.driver.find_element(By.XPATH, Locators.maleRadioButton).click()

    def clickOnAgreementButton(self):
        self.driver.find_element(By.NAME, Locators.agreementButton).click()

    def getInvalidEmailError(self):
        return self.driver.find_element(By.XPATH, Locators.invalidEmailError).text

    def getEmptyFirstNameError(self):
        return self.driver.find_element(By.XPATH, Locators.emptyFirstNameError).text

    def getEmptyLastNameError(self):
        return self.driver.find_element(By.XPATH, Locators.emptyLastNameError).text

    def getInvalidPhoneNumberError(self):
        return self.driver.find_element(By.XPATH, Locators.invalidPhoneNumberError).text

    def getNoGenderSelectionError(self):
        return self.driver.find_element(By.XPATH, Locators.noGenderSelectionError).text

    def getNoAgreedTermsError(self):
        return self.driver.find_element(By.XPATH, Locators.noAgreedTermsError).text

    def clickOnSubmitButton(self):
        self.driver.find_element(By.NAME, Locators.submitButton).click()
