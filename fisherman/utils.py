def print_red(text): print("\033[91m {}\033[00m".format(text)) 
def print_green(text): print("\033[92m {}\033[00m".format(text)) 
def print_gray(text): print("\033[97m {}\033[00m".format(text))

def validate_response(response):
    if response.status_code == 200:
        return True
    elif response.status_code == 429:
        