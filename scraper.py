import requests
from bs4 import BeautifulSoup
import smtplib
import time

userprice = 15000

URL = "https://www.amazon.se/Philips-TV-55OLED804-12-Ambilight/dp/B07RW84WLW/ref=sr_1_1?dchild=1&keywords=OLED&qid=1604865086&sr=8-1"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}

def send_email():

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")
    title = soup.find(id="productTitle").get_text()
    striptitle = title.strip()

    userpricestr = str(userprice)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("paron03@gmail.com", "pawfpupztqcoyzcq")

    msg = ("Priset på\n" + striptitle + "\n\när nu under " + userpricestr + "!" + "\n\nLÄNK:" + URL).encode("utf-8")

    server.sendmail(
        "paron03@gmail.com",
        "viking.hesse@elev.ga.ntig.se",
        msg
    )
    print("Email skickat!")

    server.quit()



def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    pricestr = (soup.find(id="price_inside_buybox").get_text())
    priceint = "".join(pricestr.split())
    price = float(priceint[0:5])


    if price <= userprice:
        send_email()

    elif price > userprice:
        print("Ej under")


    print("Check")

while True:
    check_price()
    time.sleep(3600)