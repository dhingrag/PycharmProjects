import requests
import json
import jsonpath
import pytest
import logging

FORMAT = '%(asctime)s - %(levelname)s :  %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO, filename='testoutput.log')


@pytest.mark.e2e
def test_createUser():
    base_url = 'https://reqres.in/api/users'
    file = open('/Users/charulsaxena/PycharmProjects/ProblemStatement/TestCases/postbody.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(base_url, request_json)
    assert response.status_code == 201
    response_json = json.loads(response.text)
    response_name = jsonpath.jsonpath(response_json, 'name')
    assert response_name[0] == 'clarke'


    base_url = 'https://reqres.in/api/users?page=2'
    response = requests.get(base_url)
    assert response.status_code == 200
    parsed_json_response = json.loads(response.text)
    print(parsed_json_response)
    logging.info("Passed:Delete the user Test")