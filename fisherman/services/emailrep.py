import requests

from fisherman import utils

# https://emailrep.io/docs/

BASE_URL = "https://emailrep.io/"

def issuspicious(email):
    utils.print_gray('Sending email to EmailRep')
    request_URL = "{email_rep_url}{email_addr}".format(email_rep_url=BASE_URL, email_addr=email)
    request_headers = {"Accept": "application/json"} 
    response = requests.get(request_URL, headers=request_headers)
    utils.validate_response(response)
    return response.json()['suspicious']

def isdomainsuspicious(email):
