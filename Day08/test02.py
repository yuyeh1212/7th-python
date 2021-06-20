import csv

import requests
from bs4 import BeautifulSoup

url = "https://goodinfo.tw/StockInfo/StockBzPerformance.asp?STOCK_ID=2330"
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
resp = requests.get(url, headers=headers)
resp.encoding = 'utf-8'
raw_html = resp.text

soup = BeautifulSoup(raw_html, 'html.parser')

# def list_transform_dict(payload_dict):
# for ls in payload_dict:
# return ls

payload_list = []

for index in range(4, 21):

    prefix = f'#divDetail > table > tr:nth-child({index})'
    payload_dict = {}
    payload_dict['year'] = soup.select(
        f'{prefix} > td:nth-child(1) > nobr')[0].text
    payload_dict['final_price'] = soup.select(
        f'{prefix} > td:nth-child(4) > nobr')[0].text
    payload_dict['profit'] = soup.select(
        f'{prefix} > td:nth-child(12) > nobr')[0].text
    payload_dict['profit_percentage'] = soup.select(
        f'{prefix} > td:nth-child(16) > nobr')[0].text
    print('year:', payload_dict['year'], 'final_price:', payload_dict['final_price'], 'profit:',
          payload_dict['profit'], 'profit_percentage:', payload_dict['profit_percentage'])

    headers = ['year', 'final_price', 'profit', 'profit_percentage']
    with open('payload.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, headers)
        dict_writer.writeheader()
        dict_writer.writerows(payload_list)
