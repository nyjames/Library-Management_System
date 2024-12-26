# Pytest learning lab documentation

# Unit Testing Lab: Using Pytest

## Overview
This lab will teach you how to write and execute unit tests using Pytest. You will learn to write effective test cases for individual components of a Python application, understand the testing process, and evaluate the results.

---

## Preparation Guide

### Prerequisites
Before beginning this lab, ensure you:
- Have a basic understanding of Python, functions, and classes.
- Understand what unit testing is and why it’s important.
- Have the following installed:
  - Python (version 3.8 or later)
  - Pytest (`pip install pytest`)

### Resources
Review the following resources to prepare:
- [Pytest Documentation](https://docs.pytest.org/)
- [Pytest Beginner’s Guide](https://realpython.com/pytest-python-testing/)

---

## Tutorials

### Lab Execution Documentation
#### Section 1: Step-by-Step Instructions
##### Setup:
- Ensure your Django application is running and your database is migrated.
##### Test Creation:
- Follow the instructions above to write a unit test for the Book model.
##### Run the Tests:
- Use the pytest command to execute the tests.
##### Analyze Results:
- Check if the tests pass or fail.
- For any failures, debug the code to fix issues and re-run the tests.

## Task:
- Modify the test_book_checkout test to add a test case for returning a book using the return_book method.
- Write a test to ensure books can’t be checked out twice without being returned.

### Environment Setup
1. Ensure you have Python and Pytest installed.
2. Clone the project repository:

   ```
   git clone https://github.com/csc256/fa24project-fa24project_team_4.git

   cd fa24project-fa24project

   git checkout -b unit-testing-lab

   python -m venv venv

   source venv/bin/activate  # For macOS/Linux

   venv\Scripts\activate     # For Windows

   pip install -r requirements.txt


## Writing Your First Test

1. Open the tests/ directory in the project.
2. Create a new test file named test_book_model.py.
3. Write a test for the Book model's checkout method:
   
   ''' 
   import pytest
   from books.models import Book

   @pytest.mark.django_db
   def test_book_checkout():
       # Arrange
       book = Book.objects.create(
           title="Sample Book",
           author="Author Name",
           isbn="1234567890",
           genre="Fiction",
           published_date="2023-01-01"
    )

    # Act
    book.checkout(user_id=1)

    # Assert
    assert book.checked_out_by == 1
    assert book.available is False


## Running the Test 

1. Run the test using Pytest:
   '''
   pytest tests/test_book_model.py

2. Observe the output. A passing test will display: 

'''

================== test session starts ==================
...
collected 1 item

tests/test_book_model.py .                              [100%]

=================== 1 passed in 0.10s ===================



## Conclusion
- By completing this lab, you will gain hands-on experience with Pytest, a crucial skill for testing Python applications effectively. You should now understand how to write, execute, and interpret unit tests.



