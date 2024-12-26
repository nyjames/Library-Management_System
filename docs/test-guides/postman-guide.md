# Postman learning lab documentation

# Student Lab: API Testing with Postman

# Objective

- In this lab, you will use Postman to test the API endpoints of the LBMS project, focusing on user authentication and session management. By the end of the lab, you will understand how to:

1. Send HTTP requfaests to the API endpoints.

2. Validate API responses for the login functionality.

3. Create and save Postman collections for automated testing.

## Prerequisites

- 1. clone the fa24project-fa24project_team-4 repository.

- 2. In your IDE terminal, move to the src directory.

''' 
cd src
'''

- 3. Activate your virtual environment

'''
.\venv\Scripts\activate   
'''

- 4. Install requirements.

'''
pip install -r requirements
'''

# Lab Instructions

## Step 1: Set up Postman
 - 1. Open Postman and create a new workspace for the LBMS project.

 - 2. Click New → Request, and name it "User Login Test."

 - 3. Select POST as the HTTP method.

 ## Step 2: Configuew the Login Request

 - 1. Set the request URL to your project's login API endpoint, For Example: 

 '''
 http://127.0.0.1:8000/api/login/
 '''

 - 2. In the Headers tab, add the following key-value pair: 

 '''

 Key: Content-Type  
Value: application/json 

'''

- 3. Go to the Body tab and select raw as the input format. Use the following JSON template:

'''

{
    "username": "testuser",
    "password": "testpassword123"
}

'''

## Step 3: Send the Request and Validate the Response

- 1. Click Send to submit the request.

- 2. Check the status code in the response:
     - 200 OK: Login was successful.
     - 401 Unauthorized: Login failed due to incorrect credentials.

- 3. Verify the response body includes a token or session data indicating successful authentication. Example:

'''

{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}

'''

## Step 4: Test Invalid Login Scenarios

- Repeat Step 3 with the following scenarios:

- 1. Incorrect Username

'''
{
    "username": "wronguser",
    "password": "testpassword123"
}

'''
 - Expected Response: 

   Status Code: 401 Unauthorized

   Response Body: 

   '''
   {
    "error": "Invalid username or password"
   }

   '''

- 2. Incorrect Password

'''

{
    "username": "testuser",
    "password": "wrongpassword"
}

'''

-  Expected Response: 

   Status Code: 401 Unauthorized

   Response Body: 

   '''
   {
    "error": "Invalid username or password"
   }

   '''

- 3. Missing Fields

'''
{
    "username": "",
    "password": ""
}

'''

-  Expected Response: 

   Status Code: 400 Bad Request

   Response Body: 

   '''
   {
    "error": "Both fields are required"
   }

   '''

## Step 5: Save Requests in a Collection

- 1. Create a new Collection in Postman and name it "LBMS API Tests."

- 2. Save all login requests (valid and invalid scenarios) in this collection.

- 3. Add descriptive names to each request for easy identification, e.g., "Login - Valid Credentials," "Login - Invalid Username," etc.

## Step 6: Automate Testing with Postman

- 1. In your collection, click Tests for each request and add assertions. Example:

'''
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});
pm.test("Response has a token", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData).to.have.property("token");
});

'''
- 2. Run the collection using Postman's Collection Runner to automate the tests.

## Conclusion
- Through this lab, you explored how to use Postman to test the login functionality of the LBMS project. You learned how to:

- 1. Configure and send API requests.

- 2. Validate responses for various scenarios.

- 3. Automate testing using Postman and Newman.

- API testing is an essential skill for ensuring robust backend functionality. Extend this knowledge to test other endpoints in the LBMS project, such as user registration or book management APIs.