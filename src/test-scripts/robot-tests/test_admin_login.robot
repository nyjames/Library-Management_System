*** Settings ***
Library           SeleniumLibrary
Library           DjangoLibrary

*** Variables ***
${SERVER_URL}     http://localhost:8000

*** Test Cases ***
Test Login Page
    [Documentation]   Verify that the admin login page works.
    Open Browser      ${SERVER_URL}/admin/login/    Chrome
    Input Text        id=id_username    wsv
    Input Text        id=id_password    CSC256_FA2024
    Click Button      xpath=//input[@type="submit"]
    Page Should Contain    Site administration
    Close Browser