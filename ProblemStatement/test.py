import json
import jsonpath
import requests

base_url = 'https://reqres.in/api/users'
# read i/p json file
file = open('/Users/charulsaxena/PycharmProjects/ProblemStatement/TestCases/postbody.json', 'r')
json_input = file.read()  # right now a string
# pass the input as a request body
request_json = json.loads(json_input)  # convert the string to a json body
# make a post request with json_i/p body
response = requests.post(base_url, request_json)
assert response.status_code == 201
response_json = json.loads(response.text)
response_name = jsonpath.jsonpath(response_json, 'name')
assert response_name[0] == 'clarke'

