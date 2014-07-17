from buyersguide import BuyersGuide

def main():
    bg = BuyersGuide()

    for product in bg.get_products():
        print product

    print '\nTesting single product:'
    print bg.get_product('iPhone')

if __name__ == '__main__':
    main()