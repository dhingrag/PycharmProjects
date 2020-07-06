import requests
import json
import jsonpath
import pytest
import logging

FORMAT = '%(asctime)s - %(levelname)s :  %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO, filename='testoutput.log')


@pytest.mark.CRUD
def test_get_allUsers():
    logging.info("Start:GET ALl USERS Test")
    base_url = 'https://reqres.in/api/users?page=2'
    response = requests.get(base_url)
    assert response.status_code == 200, "Response doesnt have expected Status Code"
    parsed_json_response = json.loads(response.text)
    print(parsed_json_response)
    logging.info("Passed:GET ALl USERS Test")


@pytest.mark.CRUD
def test_createUser():
    logging.info("Start:Create a new user Test")
    base_url = 'https://reqres.in/api/users'
    file = open('/Users/charulsaxena/PycharmProjects/ProblemStatement/TestCases/postbody.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(base_url, request_json)
    assert response.status_code == 201, "Response doesnt have expected Status Code"
    assert response.json()['name'] == request_json['name'], "Response doesnt have expected name "
    logging.info("Passed:Create a new user Test")


@pytest.mark.gaurav
def test_update_user():
    logging.info("Start:Update the user Test")
    base_url = 'https://reqres.in/api/users?page=2'
    file = open('/Users/charulsaxena/PycharmProjects/ProblemStatement/TestCases/postbody.json', 'r')
    json_input=file.read()
    request_body = json.loads(json_input)
    response = requests.put(base_url, request_body)
    assert response.status_code == 200, "Response doesnt have expected Status Code"
    logging.info("Passed:Update the user Test")


@pytest.mark.CRUD
def test_deleteUser():
    logging.info("Start:Delete the user Test")
    base_url = 'https://reqres.in/api/users/2'
    response = requests.delete(base_url)
    print(response.status_code)
    assert response.status_code == 204, "Response doesnt have expected Status Code"
    logging.info("Passed:Delete the user Test")
