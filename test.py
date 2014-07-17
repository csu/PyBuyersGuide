from PyBuyersGuide import BuyersGuide

def main():
    bg = BuyersGuide()
    for product in bg.get_products():
        print product

if __name__ == '__main__':
    main()