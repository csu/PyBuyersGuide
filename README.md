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