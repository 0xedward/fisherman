import argparse
import sys
import validators

from fisherman.services import apility, emailrep
from fisherman.utils import colors

def main():
    parser = argparse.ArgumentParser(description="""
    A tool to catch phishes
    
    Lookup email reputation:
    ------------------------------
    fisherman santiago@example.com
    """, formatter_class=argparse.RawDescriptionHelpFormatter, prog="fisherman")

    parser.add_argument("email", type=str,
                        help="Email you want to check the reputation of")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="View detailed results from each service queried")
    args = parser.parse_args()

    if not validators.email(args.email):
        colors.print_gray("Error: {} is not a valid email address format".format(args.email))
        sys.exit()

    if args.verbose:
        colors.print_gray("Verbose mode activated")

    emailrep_result = emailrep.issuspicious(args.email, args.verbose)
    if emailrep_result is None:
        colors.print_yellow("EmailRep does not have information the email at this time.")
    elif emailrep_result:
        colors.print_red("EmailRep has flagged the email as suspicious.")
    else:
        colors.print_green("EmailRep has not flagged the email as suspicious.")

    apility_result = apility.issuspicious(args.email, args.verbose)
    if apility_result is None:
        colors.print_yellow("Apility does not have information the email at this time.")
    elif apility_result:
        colors.print_red("Apility has flagged the email as suspicious.")
    else:
        colors.print_green("Apility has not flagged the email as suspicious.")

if __name__ == "__main__":
    main()
