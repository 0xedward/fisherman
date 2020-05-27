# Fisherman

A python3 tool for looking up an email address's reputation on [EmailRep](https://emailrep.io) and [Apility](https://apility.io/) without the need for API keys.

[![asciicast](https://asciinema.org/a/gxM8pX1R26sjePuXvtMrmRNEX.svg)](https://asciinema.org/a/gxM8pX1R26sjePuXvtMrmRNEX?loop=1&cols=95&rows=45)

## Installation
`pip install fisherman`

## Quick Start
```sh
# Query email address on all services for email reputation and output if email is suspicious
fisherman santiago@example.com

# Query email address on all services and output json responses from services
fisherman santiago@example.com -v 
```

## Usage
```sh
usage: fisherman [-h] [-v] email

    A tool to catch phishes

    Lookup email reputation:
    ------------------------------
    fisherman santiago@example.com


positional arguments:
  email          Email you want to check the reputation of

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  View detailed results from each service queried
```

## Disclaimer
This tool was hacked together in a few hours after one of my email addresses was flooded with fishy emails, so there are no unit tests and items on the todo list will be completed on a personal need basis.

## Credits
The fisherman ASCII art is from [ascii-art.de](http://www.ascii-art.de/ascii/def/fishing.txt)