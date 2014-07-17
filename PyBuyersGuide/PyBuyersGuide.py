import requests
from bs4 import BeautifulSoup
import re

class BuyersGuide():
    def __init__(self):
        html = requests.get('http://buyersguide.macrumors.com').text
        self.soup = BeautifulSoup(html)

    @staticmethod
    def parse_product(product, name=None):
        if name is None:
            name = product.find('h2').string
        suggestion = []
        for string in product.find('div', class_=re.compile('status')).strings:
            suggestion.append(string)
        days_since = int(product.find('span', class_=re.compile('count_')).string)
        average = int(product.find('div', class_="right average").find('span', class_="days").string)
        history = []
        for entry in product.find('div', class_="row recent-releases").find_all('div', class_="days"):
            history.append(int(entry.string))
        return Product(name, suggestion, days_since, average, history)

    def get_products(self):
        products = []
        for product in self.soup.find_all('div', class_="guide_content"):
            products.append(self.parse_product(product))
        return products

    def get_product(self, product_name):
        for product in self.soup.find_all('div', class_="guide_content"):
            name = product.find('h2').string
            if name == product_name:
                return self.parse_product(product, name)
        return None

class Product():
    def __init__(self, name, suggestion, days_since, average, history):
        self.name = name
        self.suggestion = suggestion
        self.days_since = days_since  # days since last release
        self.average = average
        self.history = history  # history of recent releases

    def __str__(self):
        return "Name: %s, Suggestion: %s, Days since: %s, Average: %s, History: %s" % (self.name,
                                                                                       self.suggestion,
                                                                                       self.days_since,
                                                                                       self.average,
                                                                                       self.history)