class Locators:
    firstNameField = 'FirstName'
    lastNameField = 'LastName'
    emailField = 'Email'
    phoneNumberField = 'PhoneNumber'
    maleRadioButton = '//*[@id="root"]/form/div[1]/input'
    agreementButton = 'Agreement'
    submitButton = "submitbutton"
    invalidEmailError = '//*[@id="root"]/form/p'
    emptyFirstNameError = '//*[@id="root"]/form/p[1]'
    emptyLastNameError = '//*[@id="root"]/form/p[1]'
    invalidPhoneNumberError = '//*[@id="root"]/form/p'
    noGenderSelectionError = '//*[@id="root"]/form/p'
    noAgreedTermsError = '//*[@id="root"]/form/p'
