import json
import requests

from fisherman import exceptions
from fisherman.utils import colors

# Documentation: https://apility.io/apidocs/#email-check
BASE_URL = "https://api.apility.net/bademail/"

def check_email_rep(email, verbose_flag):
    try:
        colors.print_gray('Casting line - sending email address to Apility')
        request_url = "{apility_url}{email_addr}".format(apility_url=BASE_URL, email_addr=email)
        response = requests.get(request_url)
        if response.status_code == 429:
            raise exceptions.RateLimitException()
        elif response.status_code == 404:
            colors.print_yellow("Apility does not currently have information about this email.")
        elif response.status_code == 200:
            api_data = json.loads(response.content)['response']
            if api_data['email']['score'] < 0 or api_data['address']['score'] < 0 \
                or api_data['score'] < 0:
                colors.print_red("Apility has flagged the email as suspicious.")
            else:
                colors.print_green("Apility has not flagged the email as suspicious.")
            if verbose_flag:
                colors.print_gray(json.dumps(api_data, indent=4))
    except exceptions.RateLimitException:
        colors.print_pink("The ocean has dried up. Try to catch more phish later. Apility has rate limited you.")
