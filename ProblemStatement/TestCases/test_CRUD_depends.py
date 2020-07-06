import requests
import pytest
import json
import logging

FORMAT = '%(asctime)s - %(levelname)s :  %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO, filename='testoutput.log')

def request_url(api):
    base_url = "https://reqres.in/"
    api_url = base_url + api
    return api_url


user_id = ""


@pytest.mark.CRUD
def test_get_user():
    logging.info("Start:Get All users Test")
    user_id_request = "2"
    resp = requests.get(request_url("api/users/" + user_id_request))
    assert str(resp.status_code) == '200'
    global user_id
    user_id = str(resp.json()["data"]["id"])
    logging.info("Passed:Get All users Test")


@pytest.mark.dependency(depends=['test_get_user'])
@pytest.mark.CRUD
def test_update_user():
    logging.info("Start:Update the user Test")
    update_data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    resp = requests.put(request_url("api/users/" + user_id), json=update_data)
    assert str(resp.status_code) == '200'
    assert update_data["name"] == str(resp.json()["name"])
    logging.info("Passed:Update the user Test")
