import json
import sys

import requests

args = sys.argv

def validate_number_of_arguments():
    if len(args) == 1:
        print("No arguments provided")
        exit(1)
    elif len(args) != 4:
        print("Invalid amount of arguments")
        exit(1)

validate_number_of_arguments()
src = args[1]
target = args[2]

try:
    a = float(args[3])
except ValueError:
    print("Invalid amount")
    exit(1)

if a < 0.0:
    print("Invalid amount")
    exit(1)

response = requests.get('https://api.frankfurter.app/currencies')

if response:
    cur = list(json.loads(response.text).keys())
else:
    print("Can't get the list of currencies")
    exit(1)

if src not in cur:
    print("Source currency is invalid")

if target not in cur:
    print("Target currency is invalid")


response = requests.get(f'https://api.frankfurter.app/latest?amount={a}&from={src}&to={target}')

if response:
    res = json.loads(response.text)['rates'][target]
    print(f"{a} {src} is {res} {target}")
else:
    print("Error while doing conversion")
    exit(1)
