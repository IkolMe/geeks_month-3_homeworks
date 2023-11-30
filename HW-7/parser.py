import httpx
import sqlite3
from parsel import Selector
from bs4 import BeautifulSoup

MAIN_URL = 'https://www.house.kg/snyat'
db_path = 'db/db.sqlite3'


data = []


def extract_text_from_html(html_string):
    if html_string:
        soup = BeautifulSoup(html_string, 'html.parser')
        text = soup.get_text(strip=True)
        return text

    else:
        return ''


def get_html(url):
    response = httpx.get(url)
    return response.text


def get_title(selector):
    return extract_text_from_html(selector.css('.main-wrapper .right-info .top-info .left-side .title').get())


def get_address(selector: Selector):
    return extract_text_from_html(selector.css('.main-wrapper .right-info .top-info .left-side .address').get())


def get_price_dollar(selector: Selector):
    return extract_text_from_html(selector.css('.main-wrapper .right-info .top-info .right-side '
                                               '.listing-prices-block .sep .price').get())


def get_price_local(selector: Selector):
    return extract_text_from_html(selector.css('.main-wrapper .right-info .top-info .right-side '
                                               '.listing-prices-block .sep .price-addition').get())
