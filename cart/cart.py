from django.db.models import constraints
from django.http import request
from store.models import Product


class Cart:
    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    # function to add item in cart
    def add(self, product, itemQty):
        product_id = str(product.id)
        itemQty = str(itemQty)

        # if product_id not in self.cart:
        self.cart[product_id] = itemQty

        self.session.modified = True

    # function to remove item from cart
    def delete(self, productId):
        productId = str(productId)
        del self.cart[productId]

        self.session.modified = True

    # returns the length of the cart i.e. total items in the cart
    def __len__(self):
        return len(self.cart)

    # return the products in the cart
    def get_cart_product(self):
        # product_ids = list(map(int, self.cart.keys()))
        product_ids = self.cart.keys()
        product = Product.objects.filter(id__in=product_ids)
        return product

    def get_itemQty(self):
        itemQty = self.cart
        return itemQty
