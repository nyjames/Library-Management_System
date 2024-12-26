*** Settings ***
Library           SeleniumLibrary
Library           Collections
Suite Setup       Open Browser    http://localhost:8000    Chrome
Suite Teardown    Close Browser

*** Variables ***
${BASE_URL}       http://localhost:8000/
${SIGNUP_URL}     ${BASE_URL}accounts/signup/
${LOGIN_URL}      ${BASE_URL}accounts/login/
${LOGOUT_URL}     ${BASE_URL}accounts/logout/

*** Keywords ***
User Login
    [Documentation]   Test the user login process.
    Go To    ${LOGIN_URL}
    Maximize Browser Window
    Input Text    id=id_username    wsv
    Input Text    id=id_password    CSC256_FA2024
    Click Button  xpath=//input[@type="submit"]
    Location Should Be    ${BASE_URL}

*** Test Cases ***
User Signup Test
    [Documentation]   Test already used username
    Go To    ${SIGNUP_URL}
    Maximize Browser Window
    Input Text    id=id_username    wsv
    Input Text    id=id_email       wsv@my.waketech.edu
    Input Text    id=id_age         30
    Input Text    id=id_password1   CSC256_FA2024
    Input Text    id=id_password2   CSC256_FA2024
    Click Button  xpath=//button[@type="submit"]
    Location Should Be    ${LOGIN_URL}?

User Login Test
    [Documentation]   Test the user login process.
    User Login

Invalid Login Test
    [Documentation]   Ensure invalid login attempts are handled.
    Go To    ${LOGIN_URL}
    Maximize Browser Window
    Input Text    id=id_username    fakeuser
    Input Text    id=id_password    wrongpassword
    Click Button  xpath=//input[@type="submit"]
    Page Should Contain    Please enter a correct username and password.

Logout Test
    [Documentation]   Test the logout functionality.
    [Tags]            logout
    User Login
    Click Button  xpath=//button[@type="submit"]
    Location Should Be    ${BASE_URL}