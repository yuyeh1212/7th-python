import requests

# 欲爬取的網頁網址
url = 'https://tw.stock.yahoo.com/q/bc?s=2330'

# 增加 http header user-agent 讓網站以為是正常的瀏覽使用者
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

# 發出 HTTP GET request
resp = requests.get(url, headers=headers)

# 根據 HTTP header 的編碼解碼後的內容資料（ex. UTF-8），若回傳的是 JSON 格式則可以使用 resp.json() 取得將 json 回傳值轉成 Python dict 的值
print(resp.text)