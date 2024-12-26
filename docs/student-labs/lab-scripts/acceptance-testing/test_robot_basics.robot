*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        Chrome
${URL}            https://www.wikipedia.org

*** Test Cases ***
Verify Wikipedia Search for Robot Framework
    [Documentation]    This test searches for Robot on Wikipedia and verifies that the resulting page is relevant.
    Open Browser    ${URL}    ${BROWSER}
    Wait Until Element Is Visible    id:searchInput    5s
    Input Text      id:searchInput   Robot Framework
    Submit Form     id:search-form
    Wait Until Element Is Visible    id:firstHeading    10s  # Wait for the search results to load
    Page Should Contain    Robot Framework
    [Teardown]    Close Browser

