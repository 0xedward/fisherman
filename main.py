#!/usr/bin/env python3

import argparse
import sys
import validators

from fisherman.services import emailrep 
from fisherman import utils

parser = argparse.ArgumentParser()
parser.add_argument("email", type=str, help="Email you want to check") # accept ip or direct email address later
args = parser.parse_args() # allow flag for verbose

if not validators.email(args.email):
    utils.print_gray("Error: {} is not a valid email address".format(args.email))
    sys.exit()
check_email(args.email)

# only if -d flag domain will be checked as well
domain = email.split('@')[1]
if not validators.domain(domain):
    utils.print_gray("Error: {} is not a valid domain name".format(domain))
    sys.exit()
check_domain(domain)


def check_email(email):
    if emailrep.issuspicious(email):
        utils.print_red("EmailRep has flagged the email as suspicious")
    else:
        utils.print_green("EmailRep has not flagged the email as suspicious")

def check_domain(domain):
    