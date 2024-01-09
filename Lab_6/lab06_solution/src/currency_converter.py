'''
    Program that converts certain amount of money from one currency to another.
    Three command parameters are expected:
    1) Source currency
    2) Target currency
    3) Amount to convert
'''
import json
import sys

import requests

def fetch_amount(row_amount: str) -> float:
    '''
        Converts a string to valid amount of money (non-negative integer).
    '''
    try:
        result = float(row_amount)
    except ValueError:
        raise ValueError('Passed amount is not a valid float value.')
    if result < 0:
        raise ValueError('Cannot convert negative amount of money')
    return result

def get_all_valid_currencies() -> list[str]:
    '''
        Returns list of all valid currencies.
    '''
    response = requests.get('https://api.frankfurter.app/currencies', timeout=5)
    if not response:
        raise RuntimeError('Can\'t get the list of currencies')
    return list(json.loads(response.text).keys())

def is_valid_currency(currency: str) -> bool:
    '''
        Checks if a string is valid known currency.
    '''
    currencies = get_all_valid_currencies()
    return currency in currencies

def process_arguments(args: list[str]) -> (str, str, float):
    '''
        Validates passed arguments.
    '''
    if len(args) != 4:
        raise ValueError('Invalid number of aguments passed.')
    if not is_valid_currency(args[1]):
        raise ValueError('Source currency is invalid')
    if not is_valid_currency(args[2]):
        raise ValueError('Target currency is invalid')
    return args[1], args[2], fetch_amount(args[3])

def get_converting_url(source_currency: str, target_currency: str, amount: float) -> str:
    '''
        Generates the converting url.
    '''
    return f'https://api.frankfurter.app/latest?amount={amount}&from={source_currency}&to={target_currency}'

def convert_amount(source_currency: str, target_currency: str, amount: float) -> float:
    '''
        Converts valid amount of money form valid currency to another valid currency.
    '''
    converting_url = get_converting_url(source_currency, target_currency, amount)
    response = requests.get(converting_url, timeout=5)
    if not response:
        raise RuntimeError('Error while doing conversion')
    return json.loads(response.text)['rates'][target_currency]

def __main__() -> None:
    source_currency, target_currency, amount = process_arguments(sys.argv)
    converted_money = convert_amount(source_currency, target_currency, amount)
    print(f'{amount} {source_currency} is {converted_money} {target_currency}')
