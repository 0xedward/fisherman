import json
import requests

from fisherman import exceptions
from fisherman.utils import colors

# Documentation: https://emailrep.io/docs/
BASE_URL = "https://emailrep.io/"

def check_email_rep(email, verbose_flag):
    try:
        colors.print_gray('Casting line - sending email address to EmailRep')
        request_url = "{email_rep_url}{email_addr}".format(email_rep_url=BASE_URL, email_addr=email)
        response = requests.get(request_url, headers={"Accept": "application/json"})
        if response.status_code == 429:
            raise exceptions.RateLimitException()
        elif response.status_code == 200:
            api_data = json.loads(response.content)
            if api_data['suspicious']:
                colors.print_red("EmailRep has flagged the email as suspicious.")
            else:
                colors.print_green("EmailRep has not flagged the email as suspicious.")
            if verbose_flag:
                colors.print_gray(json.dumps(api_data, indent=4))
    except exceptions.RateLimitException:
        colors.print_pink("The ocean has dried up. Try to catch more phish later. EmailRep has rate limited you.")
