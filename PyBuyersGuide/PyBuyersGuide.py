import requests
from bs4 import BeautifulSoup


class BuyersGuide():
    def __init__(self):
        html = requests.get('http://buyersguide.macrumors.com').text
        self.soup = BeautifulSoup(html)

    def get_product_names(self):
        products = []
        category_classes = ["tab-iphone", "tab-mac", "tab-other"]
        for category_class in category_classes:
            for category in self.soup.find_all('div', attrs={"class": "tab-container %s" % category_class}):
                for product in category.find_all('li'):
                    for string in product.stripped_strings:
                        products.append(string)
        return products

class Product():
    def __init__(self, name, suggestion, days_since, average, history):
        self.name = name
        self.suggestion = suggestion
        self.days_since = days_since  # days since last release
        self.average = average
        self.history = history  # history of recent releases