*** Settings ***
Library           SeleniumLibrary
Library           DjangoLibrary

*** Variables ***
${BROWSER}        Chrome
${URL}            http://localhost:8000/
${USERNAME}       testuser
${PASSWORD}       p@ssw0rd!

*** Test Cases ***
User Signup
    [Documentation]   Test the user signup process.
    Open Browser  ${URL}accounts/signup/    ${BROWSER}
    Input Text    id=id_username    ${USERNAME}
    Input Text    id=id_email       ${USERNAME}@example.com
    Input Text    id=id_age         30
    Input Text    id=id_password1   ${PASSWORD}
    Input Text    id=id_password2   ${PASSWORD}
    Click Button  xpath=//button[@type="submit"]
    Page Should Contain     Login
    [Teardown]    Close Browser


User Login
    [Documentation]   Test the user login process.
    Open Browser  ${URL}accounts/login/    ${BROWSER}
    Input Text    id=id_username    ${USERNAME}
    Input Text    id=id_password    ${PASSWORD}
    Click Button  xpath=//input[@type="submit"]
    Page Should Contain     Hello, ${USERNAME} Welcome to Homepage!
    [Teardown]    Close Browser

