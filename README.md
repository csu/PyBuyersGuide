PyBuyersGuide
=============

A Python API for the [MacRumors Buyer's Guide](http://buyersguide.macrumors.com/) for Apple products.

## Usage

    from buyersguide import BuyersGuide
    
    bg = BuyersGuide()
    
    # get all the products and all their information
    bg.get_products()
    
    # get information on one specific product
    bg.get_product('iPhone')

## Class: `Product`
### Properties
* `name` – the name of the product (str)
* `suggestion` – the suggestion for buyers (list of strs)
* `days_since` – days since the last release (int)
* `average` – the average number of days between releases (int)
* `history` – a history of how many days were between the past releases (list of ints)