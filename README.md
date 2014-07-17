PyBuyersGuide
=============

A Python API for the MacRumors Buyer's Guide for Apple products.

## Usage

    from PyBuyersGuide import BuyersGuide
    
    bg = BuyersGuide()
    
    # get all the products and all their information
    bg.get_products()
    
    # get information on one specific product
    bg.get_product('iPhone')
    
## Class: `Product`
### Properties
* `name`
* `suggestion`
* `days_since`
* `average` – the average 
* `history` – a list of how many days were between the past releases