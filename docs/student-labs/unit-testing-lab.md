# Student Lab #1: Unit Testing (Pytest)

## Introduction to Pytest
Pytest is a widely used testing framework for Python that makes writing and running tests easy. Its intuitive Python syntax makes testing accessible and efficient. Pytest is able to automatically discover and execute tests prefixed with test_ and provides detailed failure reports to help identify and fix issues quickly.

The most important element of Pytest is the assert function. You use assert to make a test pass or fail based on a condition. In the following labs, you'll learn the basics of Pytest as well as the fundamentals of **Unit Testing**.

## Lab 1: Testing Calculations with Pytest
### Preparing IDE
We recommend using VSCode as the IDE for this lab. Before beginning, ensure the VSCode extension for [Python](vscode:extension/ms-python.python) is installed. Then complete the following actions:

1\. Open a terminal in VSCode and create a virtual environment for the project by entering the following command:
```bash
python -m venv venv
```

2\. Select the virtual environment. Open Command Palette (Ctrl-Shft-P), type ***Python: Select Interpreter***, and choose the venv you created.

3\. Enter the following command in the terminal to install PyTest:
```bash
pip install pytest
```

### Part 1: Basics

Begin by creating a script called test_basics.py. Import pytest, define the test_basics() function, and assert a simple condition such as the following:
```python
import pytest

def test_basics():
    assert 1 + 1 == 2
```

Because your pytest script's name is prefixed with 'test_', you can run it by typing 'pytest' in the terminal. This will run all pytests in the project. You can also specify a specific directory or test script to run.
```bash
pytest
```
As long as your condition was true, you should see that your test passes. Now add a false condition to your test.

```python
import pytest

def test_basics():
    assert 1 + 1 == 2
    assert 1 - 1 == 2
```
When you run the test now, the test will fail and you should see the following in the failure report:
```
    def test_basics():
        assert 1 + 1 == 2
>       assert 1 - 1 == 2
E       assert (1 - 1) == 2

test_basics.py:6: AssertionError
FAILED test_basics.py::test_basics - assert (1 - 1) == 2
```

From this we can see that the test failed on line 6 when asserting 1 - 1 == 2. Correct this condition so that it returns true (i.e. 1 - 1 == 0) and run the test again. This time is should pass.

### Part 2: Unit Testing
Pytest is commonly used for Unit testing, meaning to test individual modules or functions in your project. Here's how you can do that.
Start by creating the script addition.py. Add the following code (include the mistake):
```python
def add(a, b):
    return a + a
```
Now create a new pytest called test_addition.py. Import pytest as well as 'add' from your addition module and assert the following:
```python
import pytest
from addition import add

def test_addition():
    assert add(2, 2) == 4
```
Run the pytest and you should see that, despite the error in the add function, it passes. This is why it's important to test multiple cases. Add a new case to your test
```python
assert add(2, 2) == 4
assert add(2, 3) == 5
```
Run the test again and check the failure report.
```
    def test_addition():
        assert add(2, 2) == 4
>       assert add(2, 3) == 5
E       assert 4 == 5
E        +  where 4 = add(2, 3)

test_addition.py:7: AssertionError
FAILED test_addition.py::test_addition - assert 4 == 5
```
You can see that the failure takes place in the add function. Correct the error and run the test again. Now you know how to write and execute unit tests using Pytest.

## Lab 2: Unit Testing Library Management System with Pytest
This lab will teach you how to write and execute unit tests in a real world scenerio. You will learn to write effective test cases for individual components of the Library Management application, understand the testing process, and evaluate the results.

### Preparation Guide
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

### Part 1: Step-by-Step Instructions
In this lab you'll complete the following steps:

**1\. Setup:** Ensure your Django application is running and your database is migrated.

**2\. Test Creation:** Follow the instructions to write a unit test for the Book model.

**3\. Run Tests:** Use the pytest command to execute the tests.

**4\. Analyze Results:** Check if the tests pass or fail. For any failures, debug the code to fix issues and re-run the tests.

### Task:
- Modify the test_book_checkout test to add a test case for returning a book using the return_book method.
- Write a test to ensure books can’t be checked out twice without being returned.

### Environment Setup
1\. Ensure you have Python and Pytest installed.

2\. Clone the project repository:

```
git clone https://github.com/csc256/fa24project-fa24project_team_4.git

cd fa24project-fa24project

git checkout -b unit-testing-lab

python -m venv venv

source venv/bin/activate  # For macOS/Linux

venv\Scripts\activate     # For Windows

pip install -r requirements.txt
```


### Writing Your First Test

1\. Open the tests directory in the project.

2\. Create a new test file named test_book_model.py.

3\. Write a test for the Book model's checkout method. Try it first on your own and check the following solution if you need help.
<details><summary>Solution</summary>

```python
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
        published_date="2023-01-01")

        # Act
        book.checkout(user_id=1)

        # Assert
        assert book.checked_out_by == 1
        assert book.available is False
```
</details>


### Running the Test 

1\. Run the test using Pytest:
```
pytest tests/test_book_model.py
```

2\. Observe the output. A passing test should display: 

```
================== test session starts ==================
...
collected 1 item

tests/test_book_model.py .                              [100%]

=================== 1 passed in 0.10s ===================
```

Congrats on writing your first Unit Test! If your test failed, you should examine the failure report to help you debug the problem and determine whether it is an issue with the test or the unit being tested.

## Conclusion
In this lab you learned how to use Pytest to write and execute basic tests and perform unit testing on functions in your projects. You learned how to debug test failures and the importance of writing comprehensive test cases. You also learned how to use Pytest in a real-world scenario by creating and performing unit tests for the Libarary Management System.
