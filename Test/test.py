import unittest
from selenium import webdriver
from DSRTest.Page.testPage import testPage


class test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://vladimirwork.github.io/web-ui-playground/")

    def test_checkWhenEmailIncorrectFormat(self):
        testPageObj = testPage(self.driver)
        testPageObj.inputAndClickFields("Ayodeji", "Adedeji", "ayodejiadedeji", "08160223851")
        testPageObj.clickOnMaleRadioButton()
        testPageObj.clickOnAgreementButton()
        testPageObj.clickOnSubmitButton()
        result = testPageObj.getInvalidEmailError()
        self.assertEqual(result, "Valid email is required.", "Invalid email address")
        self.driver.refresh()

    def test_checkWhenFirstNameIsEmpty(self):
        testPageObj = testPage(self.driver)
        testPageObj.inputAndClickFields("", "Adedeji", "ayodejiadedeji@gmail.com", "08160223851")
        testPageObj.clickOnMaleRadioButton()
        testPageObj.clickOnAgreementButton()
        testPageObj.clickOnSubmitButton()
        self.assertEqual(testPageObj.getEmptyFirstNameError(), "Valid first name is required.", "Empty first name field")
        self.driver.refresh()


    def test_checkWhenLastNameIsEmpty(self):
        testPageObj = testPage(self.driver)
        testPageObj.inputAndClickFields("Ayodeji", "", "ayodejiadedeji@gmail.com", "08160223851")
        testPageObj.clickOnMaleRadioButton()
        testPageObj.clickOnAgreementButton()
        testPageObj.clickOnSubmitButton()
        self.assertEqual(testPageObj.getEmptyLastNameError(), "Valid last name is required.", "Empty last name field")
        self.driver.refresh()

    def test_checkInvalidPhoneNumber(self):
        testPageObj = testPage(self.driver)
        testPageObj.inputAndClickFields("Ayodeji", "Adedeji", "ayodejiadedeji@gmail.com", "0816022385119")
        testPageObj.clickOnMaleRadioButton()
        testPageObj.clickOnAgreementButton()
        testPageObj.clickOnSubmitButton()
        self.assertEqual(testPageObj.getInvalidPhoneNumberError(), "Valid phone number is required.",
                         'Invalid phone number')
        self.driver.refresh()

    def test_checkWhenGenderIsNotSelected(self):
        testPageObj = testPage(self.driver)
        testPageObj.inputAndClickFields("Ayodeji", "Adedeji", "ayodejiadedeji@gmail.com", "08160223851")
        testPageObj.clickOnAgreementButton()
        testPageObj.clickOnSubmitButton()
        self.assertEqual(testPageObj.getNoGenderSelectionError(), "Choose your gender.",
                         'No gender selected')
        self.driver.refresh()

    def test_checkWhenTermsIsNotClicked(self):
        testPageObj = testPage(self.driver)
        testPageObj.inputAndClickFields("Ayodeji", "Adedeji", "ayodejiadedeji@gmail.com", "08160223851")
        testPageObj.clickOnMaleRadioButton()
        testPageObj.clickOnSubmitButton()
        self.assertEqual(testPageObj.getNoAgreedTermsError(), "You must agree to the processing of personal data.",
                         'Terms not agreed to')
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print('Test complete.')
