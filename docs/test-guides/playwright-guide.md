# Playwright learning lab documentation 

# Learning Lab: Automating Login Tests with Playwright

## Objective
 - Learn how to use Playwright to test the login functionality of the Library Management System (LBMS). By the end of this lab, you'll be able to:

      - Set up Playwright in your project.

      - Write automated tests to validate the login page's behavior.

      - Use Playwright's debugging tools for troubleshooting.


# Prerequisites

- Installed Node.js and npm.

- Playwright installed (npm install playwright).

- Access to the LBMS project with the login route available.

- Basic understanding of JavaScript/TypeScript.

# Lab Tasks

## Step 1: Install requirements

'''

pip instal -r requirements


'''

## Step 2: Create a New Test File

- 1. Create a folder named tests in your project root if it doesn't exist.

- 2. Inside tests, create a file named login.spec.js.

## Step 3: Write Your First Login Test

- Add the following test to verify successful login behavior:

'''

const { test, expect } = require('@playwright/test');

test('Successful login redirects to the home page', async ({ page }) => {
    // Navigate to the login page
    await page.goto('http://localhost:8000/login');

    // Fill in the login form
    await page.fill('input[name="username"]', 'testuser');
    await page.fill('input[name="password"]', 'testpassword123');

    // Submit the form
    await page.click('input[type="submit"]');

    // Check that the user is redirected to the home page
    await expect(page).toHaveURL('http://localhost:8000/home');
});

'''

## Step 4: Test for Incorrect Credentials

- Add a test to check if an error message appears when incorrect credentials are entered:

'''
test('Invalid login shows error message', async ({ page }) => {
    // Navigate to the login page
    await page.goto('http://localhost:8000/login');

    // Fill in invalid credentials
    await page.fill('input[name="username"]', 'invaliduser');
    await page.fill('input[name="password"]', 'wrongpassword');

    // Submit the form
    await page.click('input[type="submit"]');

    // Check for error message
    const errorMessage = await page.textContent('form');
    expect(errorMessage).toContain('Please enter a correct username and password.');
});

'''

## Step 5: Test for Empty Input Fields

- Verify that the form displays validation messages for empty fields:

'''

test('Empty fields show validation errors', async ({ page }) => {
    // Navigate to the login page
    await page.goto('http://localhost:8000/login');

    // Submit the form without filling any fields
    await page.click('input[type="submit"]');

    // Check for validation error messages
    const errorMessage = await page.textContent('form');
    expect(errorMessage).toContain('This field is required.');
});

'''

## Step 6: Run the Tests

- 1. Run the tests using: 

'''

npx playwright test

'''
- 2. View the results in the terminal or open the Playwright HTML report:

'''

npx playwright show-report

'''

## Step 7: Debug and Enhance 

- Use Playwright’s debugging mode to pause tests and inspect the UI:

'''

npx playwright test --debug

'''

## Conclusion

- By completing this lab, you’ve gained hands-on experience with Playwright to automate testing of the login functionality in the LBMS project. You’ve learned how to set up Playwright, write effective tests for various login scenarios, and debug issues efficiently. Automated testing ensures your application remains reliable as it evolves, providing confidence in the user authentication process.
