import json
import unittest
import requests
from unittest import mock
import src.currency_converter as currency_converter

class Tests(unittest.TestCase):
  def test_fetch_valid_amount(self):
    amount = currency_converter.fetch_amount('123.4')
    self.assertEqual(amount, 123.4)

  def test_fetch_negative_amount(self):
    with self.assertRaises(ValueError):
        currency_converter.fetch_amount('-15')

  def test_fetch_non_numeric_amount(self):
      with self.assertRaises(ValueError):
        currency_converter.fetch_amount('random')

  def test_get_converting_url(self):
    url = currency_converter.get_converting_url('BGN', 'EUR', 20)
    self.assertEqual(url, f'https://api.frankfurter.app/latest?amount=20&from=BGN&to=EUR')

  @mock.patch('requests.get')
  def test_process_arguments_with_valid_argmunets(self, mock_get):
      mock_get.return_value.text = json.dumps({"BGN": "Bulgarian Lev", "EUR": "Euro", "USD": "United States Dollar"})
      
      source_currency, target_currency, amount = currency_converter.process_arguments(['fileName', 'BGN', 'EUR', '34.5'])
      self.assertEqual(source_currency, 'BGN')
      self.assertEqual(target_currency, 'EUR')
      self.assertEqual(amount, 34.5)

  @mock.patch('requests.get')
  def test_process_arguments_with_invalid_number_of_arguments(self, mock_get):
      mock_get.return_value.text = json.dumps({"BGN": "Bulgarian Lev", "EUR": "Euro", "USD": "United States Dollar"})
      with self.assertRaises(ValueError):
        source_currency, target_currency, amount = currency_converter.process_arguments(['fileName', 'BGN', 'EUR', '34.5', 'neee'])

  @mock.patch('requests.get')
  def test_process_arguments_with_invalid_argmunets(self, mock_get):
      mock_get.return_value.text = json.dumps({"BGN": "Bulgarian Lev", "EUR": "Euro", "USD": "United States Dollar"})
      with self.assertRaises(ValueError):
        source_currency, target_currency, amount = currency_converter.process_arguments(['fileName', 'RND', 'EUR', '34.5'])

  @mock.patch('requests.get')
  def test_process_arguments_with_invalid_currency_names(self, mock_get):
      mock_get.return_value = None
      with self.assertRaises(RuntimeError):
        source_currency, target_currency, amount = currency_converter.process_arguments(['fileName', 'RND', 'EUR', '34.5'])


  @mock.patch('requests.get')
  def test_convert_amount(self, mock_get):
      mock_get.return_value.text = json.dumps({"amount":20.0,"base":"BGN","date":"2024-01-08","rates":{"EUR":10.226}})
      converted_value = currency_converter.convert_amount('BGN', 'EUR', 20)
      self.assertEqual(converted_value, 10.226)

  @mock.patch('requests.get')
  def test_convert_amount_with_requestError(self, mock_get):
      mock_get.return_value = None
      with self.assertRaises(RuntimeError):
        converted_value = currency_converter.convert_amount('BGN', 'EUR', 20)


  
if __name__ == '__main__':
    unittest.main()

# Execute following from lab06_solution:
# pylint src/currency_converter.py --rcfile ../lab06.pylintrc -> check clean code
# python3 -m unittest  tst.test -v                            -> run tests 
# python3 -m coverage run tst/test.py                         -> prepare test coverage report
# coverage report -m                                          -> show test coverage report