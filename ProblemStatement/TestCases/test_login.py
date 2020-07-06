import requests
import pytest
import logging

FORMAT = '%(asctime)s - %(levelname)s :  %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO, filename='testoutput.log')


# Successful login case
@pytest.mark.login
def test_login_success():
   logging.info("Start:Successful Login Test")
   login_details = {
      "email": "eve.holt@reqres.in",
      "password": "cityslicka"
   }
   resp = requests.post('https://reqres.in/api/login', json=login_details)
   if resp.status_code != 200:
      raise Exception('POST /login/ {}'.format(resp.status_code))
   print('login success and token: {}'.format(resp.json()["token"]))
   logging.info("Passed:Login Test")


# UnSuccessful login case
@pytest.mark.login
def test_login_unsuccessful():
   logging.info("Start:UnSuccessful Login Test")
   login_details = {}
   resp = requests.post('https://reqres.in/api/login', json=login_details)
   if resp.status_code != 400:
      raise Exception('POST /login/ {}'.format(resp.status_code))
   print('login not successfull')
   logging.info("Passed:UnSuccessful Login Test")