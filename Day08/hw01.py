import requests
from bs4 import BeautifulSoup
import csv
import os.path

stock_id = input('please enter stock ID:')
url = f'https://goodinfo.tw/StockInfo/StockDetail.asp?STOCK_ID={stock_id}'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

resp = requests.get(url, headers=headers)
resp.encoding = 'utf-8'
raw_html = resp.text
soup = BeautifulSoup(raw_html, 'html.parser')

data = [stock_id]
# 在程式碼前後try…except錯誤機制跳過空值
try:
    s1 = soup.select(
        'body > table:nth-child(8) > tr > td:nth-child(3) > table > tr:nth-child(1) > td > table > tr:nth-child(1) > td:nth-child(1) > table > tr:nth-child(1) > td > table > tr > td:nth-child(5) > nobr')[0].text
    data.append(s1)
except IndexError:
    pass
s2 = soup.select(
    'body > table:nth-child(8) > tr > td:nth-child(3) > table > tr:nth-child(1) > td > table > tr:nth-child(1) > td:nth-child(1) > table > tr:nth-child(3) > td:nth-child(1)')[0].text
data.append(s2)
s3 = soup.select(
    'body > table:nth-child(8) > tr > td:nth-child(3) > table > tr:nth-child(1) > td > table > tr:nth-child(1) > td:nth-child(1) > table > tr:nth-child(3) > td:nth-child(7)')[0].text
data.append(s3)
s4 = soup.select(
    'body > table:nth-child(8) > tr > td:nth-child(3) > table > tr:nth-child(1) > td > table > tr:nth-child(1) > td:nth-child(1) > table > tr:nth-child(3) > td:nth-child(8)')[0].text
data.append(s4)
s5 = soup.select(
    'body > table:nth-child(8) > tr > td:nth-child(3) > table > tr:nth-child(1) > td > table > tr:nth-child(1) > td:nth-child(1) > table > tr:nth-child(3) > td:nth-child(4)')[0].text
data.append(s5)
s6 = soup.select(
    'body > table:nth-child(8) > tr > td:nth-child(3) > table > tr:nth-child(1) > td > table > tr:nth-child(1) > td:nth-child(1) > table > tr:nth-child(5) > td:nth-child(1)')[0].text
data.append(s6)
s7 = soup.select(
    'body > table:nth-child(8) > tr > td:nth-child(3) > table > tr:nth-child(2) > td:nth-child(1) > div:nth-child(6) > div > table > tr:nth-child(3) > td:nth-child(3) > nobr')[0].text
data.append(s7)
s8 = soup.select(
    'body > table:nth-child(8) > tr > td:nth-child(3) > table > tr:nth-child(2) > td:nth-child(1) > div:nth-child(9) > div > table > tr:nth-child(2) > td:nth-child(5) > nobr')[0].text
data.append(s8)
s9 = soup.select(
    'body > table:nth-child(8) > tr > td:nth-child(3) > table > tr:nth-child(2) > td:nth-child(1) > div:nth-child(9) > div > table > tr:nth-child(2) > td:nth-child(7)')[0].text
data.append(s9)
print(data)

headers = ['股票代號', '日期', '成交價', '最高價', '最低價',
           '漲跌幅', '成交張數', '五日累計漲跌幅', '外資連買連賣', '外資持股比']

if os.path.isfile('StockInquiry.csv') == False:
    with open('./StockInquiry.csv', 'a') as output_file:
        dict_writer = csv.DictWriter(output_file, headers)
        # 寫入標題
        dict_writer.writeheader()

with open('./StockInquiry.csv', 'a') as output_file:
    writer = csv.writer(output_file)
    writer.writerow(data)
