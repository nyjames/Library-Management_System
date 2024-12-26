# Applicaton Development Design Requirements
- Maintainability: The application should be maintainable, with well-documented code and a clear structure.
- Design Requirement: The application should adhere to good software design principles, and be scalable.
- Testability and Robustness Design
   - Testability Ease
      - The application should be structured to facilitate unit testing with Pytest.
      - Functions and methods should be designed to be easily mockable and testable.
      - Dependencies should be injected wherever possible to enable isolation of components during testing.
   - Exception Handling
      - The application should handle exceptions and errors gracefully.
      - Clear and informative error messages should be provided to the user.
      - Logging should be implemented to capture and trace errors for debugging purposes.
- The application must use at least one public APIs, (Examples: JokeAPI, NewsAPI, REST Countries API, etc.) for the application. 
- It should have at least 4 Application API's.

    - Example:
```
Routes:
GET /api/tasks: Returns all tasks.
GET /api/tasks/int:task_id: Returns a single task by ID.
POST /api/tasks: Creates a new task. The request must contain a JSON body with at least a title field.
PUT /api/tasks/int:task_id: Updates an existing task. The request body can include title, description, and done.
DELETE /api/tasks/int:task_id: Deletes a task by ID
``` 
> [!IMPORTANT]
> Add features as neccessary to demonstrate the minimum testing requirements below (Selenium and Playwright, API testing, and Robot Framework).

# Selenium and Playwright Requirements

The following are **mandatory/required** to test in your application using Selenium and Playwright (and demonstrate in your respective Student Labs that your create).  

> [!NOTE]
> This means your web application must have the entities to be tested and features should be added as neccessary to be able to test.  For example,  to perform a form submission test your application must have a form.  This means your web application must have a form that can be tested.  

> [!IMPORTANT] 
> You will need to create user stories for your application for testing. 

They should cover the following:

- Form Submissions: Test form filling, submissions, and validation messages.
- Link and Button Clicks: Automate clicking on various links and buttons to ensure they lead to the correct actions or pages.
- Dropdown Menus: Test interactions with dropdown menus, including selecting various options.
- Mouse Actions: Simulate mouse actions like clicks, double-clicks, hover, and drag-and-drop.
- Keyboard Inputs: Test keyboard interactions, including text input and keyboard shortcuts.
- Layout Testing: Check the layout and positioning of UI components.
- Page Navigation: Test navigation between different pages or sections of the application.
- Data Entry and Retrieval: Test CRUD (Create, Read, Update, Delete) operations on data.
- Data Validation: Ensure the correctness of data processing and output.
- Error Messages: Test for correct error messages under various error conditions.
- Handling Exceptions: Ensure the application handles unexpected exceptions gracefully.

# API Testing Requirements
- Ensure that all API endpoints function correctly using POSTMAN. The application should use the Requests library.
- Test to ensure that the application handles exceptions and errors gracefully, providing useful feedback to the user.
- Create user stories for the application for the API testing.
- Test the application to handle errors gracefully and maintain data integrity.

# Requirements for Robot Framework Testing

- Implement tests for user interface, database interactions, and REST APIs applications.
- Develop test cases to validate functional requirements of the application.
- User Stories: Create automated acceptance tests to ensure the application meets all functional requirements.
- Test error handling and recovery processes.
- User Stories: Test the application to handle errors gracefully and maintain data integrity.
- Maintain comprehensive documentation of test cases, results, and any anomalies.
- Generate reports using Robot Framework's reporting capabilities.

## Examples of Generic User Stories for Development

- Interact with API
  - As a user, I want to interact with a free API to retrieve and view data based on my inputs or selections.
- Handle Various Data Types
  - As a user, I want to see different types of data (text, images, etc.) handled appropriately by the application.
- Customizable Queries
  - As a user, I want to customize my queries or requests to the API to filter or search for specific information.
- Error and Exception Handling
  - As a user, I want the application to provide clear error messages for invalid inputs or API errors, helping me understand what needs to be corrected.
- Responsive and Efficient Performance
  - As a user, I expect the application to perform efficiently, with minimal delays or loading times.
- Documentation and Help
  - As a user or developer, I want the application to include documentation or help options so that I can easily understand how to use or modify it.
- Adaptability and Scalability
  - As a developer, I want the application structure to be adaptable and scalable, allowing for the integration of additional features or APIs in the future.
- Postman Testing for Interfaces
  - As a developer, I want to create Postman tests that are applicable to either CLI or web-based endpoints of the Python application.
- Documentation for Interfaces
  - As a developer, I want comprehensive documentation that covers both CLI and web usage of the application, including API endpoint details.
- Environment Setup for CLI/Web API Testing
  - As a developer, I need to set up environments in Postman for testing either CLI commands or web API requests effectively.

### Example of ONE modification based on example group API project

- The application must provide top news headlines from the News API based on country and category.
   - User Story: As a user, I want to be able to specify the country and category for the news so that I can receive relevant top headlines.

