# ProblemStatement

Problem statement is a project to have two main functions on public API - https://reqres.in
1. Login
2. CRUD Operation

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) and requirements.txt to install the libraries required.

```bash
pip install -r requirements.txt
```
## Usage
Command to run all tests

```bash
pytest TestCases
```
Command to skip a test via decorators(decorate a test method with this to skip a test)
@pytest.mark.skip, ( skipped one will not run)- see shows in execution summary
```bash
pytest TestCases
```
Grouping test cases together
Decorate a test method with this to group them
@pytest.mark.login and @pytest.mark.CRUD

For running  test
```bash
pytest -m CRUD -v TestCases
pytest -m login -v TestCases
``` 

For running all tests apart from CRUD, run below
```bash
pytest -m " not CRUD" -v TestCases
```
For running all tests apart from login 
```bash
pytest -m " not login" -v TestCases
```


Reporting

First it generates json formatted reports
```bash
pytest --alluredir "/Users/charulsaxena/PycharmProjects/ProblemStatement/Reports" TestCases
````
Next we will convert it in to HTML formatted reports using allure module
```bash
allure serve "/Users/charulsaxena/PycharmProjects/ProblemStatement/Reports"
```

For Running tests with logging override, run below 
```bash
pytest -m CRUDSSS -s
pytest -m CRUDSSS -s --log-cli-level=DEBUG

```
## Contributing
All the contributions have been made by Gaurav Dhingra as a part of Assignment 
from PredictSpring







