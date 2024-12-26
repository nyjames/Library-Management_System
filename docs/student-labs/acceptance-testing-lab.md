# Student Lab #4: Acceptance Testing (Robot)

## Introduction to Robot
Robot Framework is an open-source automation framework that can be used for acceptance testing. It features easy-to-read, plain-text syntax and integrates well with libraries like Selenium. 

In these labs you'll learn how to set up Robot, create a simple test case, and use it to test a web application's functionality. You'll also learn the fundamentals of **Acceptance Testing.**

## Lab 1: Robot Basics
### Preparing IDE
1\. Create and select a virtual environment in VSCode.

2\. Install Robot Framework and its Selenium Library:
```
pip install robotframework
pip install robotframework-seleniumlibrary
```
3\. Ensure ChromeDriver is in PATH (Refer to Student Lab #3: UI Testing)

4\. Verify installation:
```
robot --version
```

### Part 1: Setting up Robot Script
Robot requires some basic structure to initialize and execute tests. Create a script 'test_robot_basics.robot' and add the following lines.

```
*** Settings ***
# Import the SeleniumLibrary to interact with web browsers
Library           SeleniumLibrary

*** Variables ***   
# Define any variables here to be used in your test cases
${BROWSER}        Chrome

*** Test Cases ***
# Write your test cases here. Each test case should start with a unique name
```
### Breakdown:
#### **Settings**
This section is used to import libraries, resource files, or other dependencies required for your test suite.

#### **Variables**
Use this section to define global variables that can be reused across your test cases. For instance, you could store URLs, credentials, or other constants here.

#### **Test Cases**
This is where the actual test logic resides. Each test case starts with a unique name and is followed by the sequence of steps to be executed.

### Part 2: Wikipedia search with Robot
Now we'll search Wikipedia for more info on Robot.

1\. Continuing in test_robot_basics.robot, create variables for Youtube's url and the search term you want to use.
```
*** Variables ***
${BROWSER}        Chrome
${URL}            https://www.wikipedia.org
```

2\. Now we'll open Wikipedia using our ChromeDriver.
```
*** Test Cases ***
Verify Wikipedia Search for Robot Framework
    [Documentation]    This test searches for "${SEARCH_TERM}" on Wikipedia and verifies that the resulting page is relevant.
    Open Browser    ${URL}    ${BROWSER}
```

3\. Now perform the search and wait for the next page to load. Inspect Wikipedia to find the correct html ID's.
```
Wait Until Element Is Visible    id:searchInput    5s
Input Text      id:searchInput    Robot
Submit Form     id:search-form
Wait Until Element Is Visible    id:firstHeading    10s  # Wait for the search results to load
```

4\. Verify the the page is relevant and close the browser. 
```
Page Should Contain    Robot Framework
[Teardown]    Close Browser
```
5\. Run the test from terminal.
```
robot test_robot_basics.robot
```
The test should fail since the search term was too broad. If you click on the automatically generated log report, you should see extensive information including screenshots showing what happened. Update your code to search more specifically for 'Robot Framework'.
```
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
```

With this final code, you have successfully written your first Robot test. Congrats!

## Lab 2: Acceptance Testing Library Management System with Robot
Acceptance testing is conducted to determine whether a system meets the business requirements and is ready for delivery to end users. It validates that the software functions as intended in real-world scenarios. In our Acceptance Testing we'll verify that users are able to login to the Libary Management System and search for books.

### Preparation Guide
Before beginning this lab, ensure you:
- Have a basic understanding of Python, functions, and classes.
- Understand what Acceptance testing is and why it’s important.
- Have the following installed:
  - Python (version 3.8 or later)
  - Robot Framework (`pip install robotframework`)
  - Robot Selenium Library (`pip install robotframework-seleniumlibrary`)
  - Robot Django Library (`pip install robotframework-djangolibrary`)
  - ChromeDriver (Added to PATH)

***NOTE:*** Use `pip install -r requirements.txt` to install any missing dependencies  

### Environment Setup
1\. Ensure you have Python and Pytest installed.
2\. Clone the project repository:

```
git clone https://github.com/csc256/fa24project-fa24project_team_4.git

cd fa24project-fa24project

git checkout -b acceptance-testing-lab

python -m venv venv

source venv/bin/activate  # For macOS/Linux

venv\Scripts\activate     # For Windows

pip install -r requirements.txt
```

### Part 1: Test User Registration and Login
First we'll design a test to ensure that users can register accounts and login.

1\. Create a script named 'test_signup_login.robot'.

2\. Import Selenium and Django libraries.
```
*** Settings ***
Library           SeleniumLibrary
Library           DjangoLibrary
```

3\. Create variables for Browser, URL, Username, and Password.
```
*** Variables ***
${BROWSER}        Chrome
${URL}            http://localhost:8000/
${USERNAME}       testuser
${PASSWORD}       p@ssw0rd
```

4\. Write a test that opens the sign up page and attempts to register an account. Try it first on your own and check the following solution if you need help.
<details><summary>Solution</summary>

```
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
```
</details>  

5\. Write a second test that opens the login page and attempts to login to that account. Verify that login is successful. Try it first on your own and check the following solution if you need help.
<details><summary>Solution</summary>

```
User Login
    [Documentation]   Test the user login process.
    Open Browser  ${URL}accounts/login/    ${BROWSER}
    Input Text    id=id_username    ${USERNAME}
    Input Text    id=id_password    ${PASSWORD}
    Click Button  xpath=//input[@type="submit"]
    Page Should Contain     Hello, ${USERNAME} Welcome to Homepage!
    [Teardown]    Close Browser
```
</details>  

Now start the server: 
```
python manage.py runserver
```
And run the test:
```
robot test_signup_login.robot
```
Good work creating your first acceptance test with Robot!

### Part 2: Catalog Search
Now we'll verify that users can reach the catalog from the home page and search for books
1\. Create a script named 'test_catalog_search.robot'.

2\. Import Selenium and Django libraries.

```
*** Settings ***
Library           SeleniumLibrary
Library           DjangoLibrary
```
3\. Create variables for Browser, URL, Book Title, and Book ISBN.

```
*** Variables ***
${BROWSER}        Chrome
${URL}            http://localhost:8000/
${TITLE}          The Plague
${ISBN}           9780679720218 
```

4\. Write a test that opens the homepage, navigates to catalog, searches for book title, and verifies presence of corresponding ISBN. Try it first on your own and check the following solution if you need help.
<details><summary>Solution</summary>

```
*** Test Cases ***
Test Search Function
	[Documentation]   Verify that user can navigate from home page to catalog and that the search function works and brings up relevant results.
	Open Browser  	${SERVER_URL}	Chrome
	Maximize Browser Window                 # Catalog link may be obscured if window is not large enough
	Wait Until Element Is Visible	id:navbarNav   3
	Click Link    	Catalog
	Wait Until Element Is Visible	name:search	3
	Input Text    	name:search	${TITLE} 	# Search for book titled '${TITLE}'
	Press Keys    	name:search	ENTER
	Page Should Contain	${ISBN}        		# Verify that book with ISBN corresponding to title has been brought up
	[Teardown]	Close Browser
```

</details>

Run the test. Good work creating your second acceptance test with Robot! Now you've tested the most important functions of the Library Management System from the user's perspective.

## Conclusion
In this lab you learned how to use Robot for web automation and testing. You learned the fundamentals of navigating, interacting with, and testing web pages through Robot's keyword-driven syntax. You also learned how to use Robot in a real world scenario by creating and performing acceptance tests for the Library Management System.


