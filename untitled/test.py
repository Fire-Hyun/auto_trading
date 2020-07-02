import pandas as pd
import requests


html = requests.get('https://finance.naver.com/item/coinfo.nhn?code=068270')
table = pd.read_html(html.text)
print(table[0][2])
