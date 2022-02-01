from bs4 import BeautifulSoup
from decimal import Decimal
import requests


def convert(amount, cur_from, cur_to, date, requests):
    params = {'date_req': date}
    response = requests.get('https://cbr.ru/scripts/XML_daily.asp', params)  # Использовать переданный requests
    rates = BeautifulSoup(response.text, 'lxml')

    if cur_from == 'RUR':
        val_from = Decimal(1)
    else:
        nominal_from = int([i.nominal.text for i in rates.find_all('valute')
                            if i.charcode.text == cur_from][0].replace(',', '.'))
        val_from = Decimal([i.value.text for i in rates.find_all('valute')
                      if i.charcode.text == cur_from][0].replace(',', '.')) / nominal_from

    amount_from = amount * val_from

    nominal_to = int([i.nominal.text for i in rates.find_all('valute')
                      if i.charcode.text == cur_to][0].replace(',', '.'))
    val_to = Decimal([i.value.text for i in rates.find_all('valute')
                      if i.charcode.text == cur_to][0].replace(',', '.'))


    result = amount_from / (val_to / nominal_to)

    return result.quantize(amount)  # не забыть про округление до 4х знаков после запятой

print(convert(Decimal("1000.1000"), 'ZAR', 'KRW', "26/02/2018", requests))