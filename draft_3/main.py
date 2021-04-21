
import requests
import lxml
from bs4 import BeautifulSoup
import smtplib


ZILLOW_ONE = 'https://docs.google.com/forms/d/e/1FAIpQLSe6lAosmVKRF8Cv-CfP2' \
             'FvNDnwyVwfJw3hvbUYpygxYjhfJWg/viewform?usp=sf_link'

url = "https://www.amazon.com/Monster-Hunter-Rise-Nintendo-Switch/dp/B08JJ37XVW/" \
      "ref=sr_1_1_sspa?crid=51GIU65E8X8Z&dchild=1&keywords=monster+hunter+rise&qid=" \
      "1618679740&sprefix=monster+hunter+%2Caps%2C241&sr=8-1-spons&psc=1&spLa=" \
      "ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNUVGMFY2QTdIUkYzJmVuY3J5cHRlZElkPUEwNDc1MTUzMVc4S1l" \
      "BTlVaU1dORSZlbmNyeXB0ZWRBZElkPUEwMzEwNzU0M0dWQ1NTTEszQjFWOSZ3aWRnZXROYW1lPXNwX2F0Z" \
      "iZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,ja;q=0.6,zh-TW;q=0.5"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())
with open("output1.html", "w") as file1:
    file1.write(str(soup))

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)