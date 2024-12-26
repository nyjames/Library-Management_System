# CSC 256 Group Project

## Project Overview

This project is an intensive team-based educational venture where students will will work together to design and develop a web application using Python and web technologies. As part of the development process parallel testing will be implemented to ensure continuous quality assurance. 

You will then create student labs to demonstrate and teach how to use testing tools and document test coverage.

The application will evolve throughout the project as neccessary to showcase the different testing tools and types required. Development will follow Agile Methodology Principles.

## Objectives

1. Collaborative Development: Students will work in teams to design and develop a functional web application.
2. Testing and Quality Assurance: Students will implement various types of tests to ensure the reliability and functionality of the application.
3. Test Coverage: Achieve and document a test coverage requirement of 70-80%.
4. Documentation and Demonstration: Students will create documentation to include Educational Student Labs, Test Plans, Software Development Documents  demonstrating good software development practices and software quality assurance
5. Effectively use automated testing tools to complete Unit, UI, API and Acceptance Testing. 

## Minium Development Design Requirements and Testing Requirements. 
> [!IMPORTANT]
> See `Minimum Design and Testing Requirements.md` for more details on Minimum Design and Testing Requirements. 

## Project Structure
- **Sprints:** 
  - The project will be divided into sprints, each with specific goals and deliverables. This approach will help manage the development process and allow for regular assessment and feedback.  
  - Each Team will create their own sprint schedule and sprint goals.  These will be documented in the Team GitHub repository, Issues and Project Board. An example of a sprint schedule, is shown in this document below.  A more detailed one can be found in the `example_project_breakdowns.md` file.
- **Parallel Testing:** Testing will be integrated into each sprint, allowing for continuous validation of the application as new features are developed.

## Testing Tools and Types

- **Parallel Testing:** Testing will be integrated into each sprint, allowing for continuous validation of the application as new features are developed.

- Unit Testing
  - Purpose: Unit tests are designed to test individual components or functions in isolation. They ensure that each part of the code works as intended.
  - Tool: Pytest
  - Students will create test cases using `Pytest` to validate the functionality of various functions and modules within the application. These unit test cases will be documented and organized into test suites to ensure thorough coverage and understanding of isolated components. 

- UI Testing
  - Purpose: UI tests (end-to-end or acceptance tests) simulate user interactions with the application to ensure that the UI behaves correctly and the application works as a whole from the user's perspective.
  - Tool: Selenium, Playwright
  - Students will create test cases using `Selenium` and `Playwright` to automate browser interactions. These UI test cases will be organized into test suites to validate that the application functions correctly from the user's point of view, covering various user scenarios and interface elements.

- API Testing
  - Purpose: API tests ensure that the backend services and endpoints behave as expected. They validate the correctness and performance of the API.
  - Tool: Postman, Requests
  - Students will create test cases using `Postman` and the `requests` library in Python to validate the application's API endpoints. These API test cases will be organized into collections and suites, ensuring the endpoints return the expected responses and handle edge cases properly.

- Acceptance Testing
  - Purpose: Acceptance tests verify that the entire system meets the business requirements and works as intended from an end-user perspective. They are used to validate new features or changes to ensure they meet the specified criteria.
  - Tool: Robot Framework
  - Students will create test cases using `Robot Framework` to ensure that the application meets the predefined requirements and works as expected in real-world scenarios. These test cases will be organized into test suites, covering various user stories and business rules to ensure complete coverage and correctness.

## Test Coverage Documentation

- Test Coverage Tools: Use tools such as `SonarQube`, `coverage.py` or `pytest-cov` to measure and document test coverage.
  - Required Test Coverage Levels: **70-80%**
  - An example of a test coverage report can be found in the `example_code_coverage.md` file.
- Students will learn to use these tools to generate coverage reports and understand the areas of the application that are well-tested and those that require additional tests.  Coverage reports will be documented and placed in the test plan, test report, and GitHub repository.

## Educational Student Labs

You will create educational student labs to instruct other students in using the tools and types described in the above sections. These labs will demonstrate and teach how to use testing tools and document test coverage.  The final educational student labs required are:

- Unit Testing Lab: The Unit Testing Studet Lab will be representative of the project and the tools you have learned to use.  The lab will demonstrate your ability to use `Pytest` effectively.

- API Testing Lab: The API Testing Student Lab will be will be representative of the project and the tools you have learned to use. The lab will demonstrate your ability to use `Postman` and the `Requests` library effectively.

- UI Testing Lab: The UI Testing Student Lab will be representative of the project and the tools you have learned to use. The lab will demonstrate your ability to use `Selenium` and `Playwright` effectively.

- Acceptance Testing Lab: The Acceptance Testing Student Lab will be used for the final deliverable and is a representative of the project and the tools you have used.  The lab will demonstrate your ability to use `Robot Framework` effectively.

**Each Educational Student Lab will include:**
- Preparation Guides. Outline pre-lab activities, required readings or resources, and prerequisite knowledge or skills.
- Tutorials: Step-by-step guides to assist students in setting up the environment, understanding the tool's functionalities, and executing the labs.
- Lab Execution Documentation: Document the execution process
  - Section 1: Step by step instructions with screen shots creating the neccessary test suite.
  - Section 2: Student Assessement where the student will demonstrate their understanding of how to use the tool effectively. 

## Collaboration and Teamwork

- Students will work in teams:
  - to design and develop a functional web application.
  - to implement various types of tests to ensure the reliability and functionality of the application.
  - to create labs that demonstrate the use of testing tools and document test coverage.
  - and will use GitHub, GitHub Issues and Projects to manage the project
  - will use MS Teams and GitHub to communicate with each other. `Issues` and `Projects` should be regularly updated.
- When the project is completed all work will be documented in the GitHub repository.
   - The final documentation, testing and code will be merged into the `main` branch.  There should be no final deliverables in any branch besides the `main` branch.  
   - Code that has issues or is still in the development process will not be merged into the `main` branch. These branches will remain and this should be reflected in both issues, and the presentation. All other branches (that have been merged with `main`) should be removed. 
   - The presentation should reflect what was merged and what was not with the reason for not merging.

## Group Final Deliverables

- A well-organized code repository with all code, tests, and documentation.
  - Functional Web Application: A fully developed web application with features added **incrementally** over the sprints. (This will be assessed by reviewing Pull Request, etc in GitHub.)
  - Comprehensive Test Suite: A compehensive test suite of Unit, UI, API and Acceptance Tests ensuring the application meets quality standards to include a comprehensive Test plan.
  - Test Coverage Reports: Detailed reports demonstrating the test coverage achieved using the designated tools.
- Presentation: A comprehensive presentation of the project. The presentation should include the following: Overview and Summary of Project, Lessons learned, Challenges, and Key Learning Outcomes.The presentation will be submitted to `Blackboard` as well as in the repository. Each group will present this in Teams to other Teams.
- Educational Student Labs: Labs should be submitted to `Blackboard` as well as in the repository. 

## Assessments

### Individual Deliverables

Peer Evaluations, Lead Evaluation and Updates as required

###  Group Project Grade:
Group Grades are based on collaboration (evaluated via GitHub and Teams usage) and the quality of the final deliverables.  **Note:** Individual project grades will have an additional factor used in the calculation: Results of Peer Evaluations.

#### Collaboration Assessment

- Participation in interactions and contributions on GitHub and Microsoft Teams.
- Code, documentation, testing will be reviewed for active participation the project. Areas such as who is doing code, testing and documentation reviews and providing feedbacks.  In addition, pull requests will be reviewed for active participation.
- Ensuring effective team collaboration in planning and decision-making. The `projects` and `Issues` tab will be reviewed for active participation.

#### Code Quality and Documentation

- **Code Review:** Ensuring code adheres to best practices and is well-documented.
- **Documentation:** Clear and comprehensive documentation for each development and testing phase.

#### Testing and Problem Solving

- **Testing:** Effective and thorough testing practices, covering all required aspects.
- **Problem Solving:** Demonstrating problem-solving skills in addressing challenges.

#### Educational Student Labs

- **Content Quality and Relevance:** Evaluate how accurately and comprehensively the lab covers the software testing tools. It should include essential features, best practices, and real-world applications.
- **Instructional Design:** Structure and organization of the lab. It should have a clear, logical flow that builds from basic concepts to more advanced ones.
- **Hands-On Components:** Evaluate the quality and relevance of the exercises and projects. They should allow students to apply concepts in real or simulated environments.
- **Learning Outcomes:** Does the lab have clearly defined learning outcomes. Students should know what skills and knowledge they are expected to gain.

### Individual Project Grade 
Individual Project Grades will be based on the following criteria:
- Peer Evaluations
- Group Grade

** See `peer_evals.md` for more details. **

## EXAMPLE ONLY: Phases of the Project (Your team may differ)

### Sprint 1: Project Planning and Preparation

- Initial Project Design and Requirements (See `web_applications_ideas_free-apis.md` and `example_project_breakdowns.md`)
- Set up project repository and development environment
- Implement user authentication (sign up, login, password reset) for your web application
- Basic project structure and initial UI design
- Test Plan and Test Cases started
- Create Unit Tests to test individual components or functions in isolation
- Start to validate APIs (Postman/Requests Library)

### Sprint 2: Add New Features and APIs

- Continue to add Features per the project schedule and write unit tests with `pytest`
- Continue to develop APIs for the project
- Implement API testing for each feature
- Continue to develop the UI
- Update Test Plan and test cases
- Continue API testing
- Start UI testing

### Sprint 3: Add New Features as Needed to Showcase Required Testing Tools (Postman, Selenium, Playwright, Robot Framework)

- Continue to add Features per the project schedule and write unit tests with `pytest`
- Continue to develop APIs for the project 
- Implement API testing for each feature
- Continue to develop and enhance the UI
- Start creating `Robot Framework` Collections
- Extend UI testing as needed
- Update Test Plan, write test cases, continue testing (API testing and UI Testing) 

### Sprint 4: Testing with Robot Framework

- Continue to add Features per the project schedule and write unit tests with `pytest`
- Implement Acceptance Testing using `Robot Framework`
- Implement API testing for each feature
- Finalize the UI and enhance user experience
- Prepare Final Documentation and Presentation
- Finalize Student Labs
  - Unit Testing Lab (Pytest)
  - UI Testing (Selenium and Playwright)
  - API Testing (Postman and Requests)
  - Acceptance Testing (Robot Framework)
