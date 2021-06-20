import pandas as pd

movie = {
    '名稱': ['名偵探柯南', '復仇者聯盟', '那些年'],
    '票房金額(新台幣)': [1452324, 2324739, 1416601],
    '類別': ['動畫', '動作', '文藝']
}

df = pd.DataFrame(movie)

data = df.loc[1, '票房金額(新台幣)']
print(data)
