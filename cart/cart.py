from store.models import Product

class Cart():
    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart
    
    def add(self,product,itemQty):
        product_id = str(product.id)
        itemQty = str(itemQty)

        if product_id not in self.cart:
            self.cart[product_id] = (itemQty)
                
        self.session.modified = True
    
    def __len__(self):
        return len(self.cart)

    def get_cart_product(self):
        # product_ids = list(map(int, self.cart.keys()))
        product_ids = self.cart.keys()
        product = Product.objects.filter(id__in=product_ids)
        return product
    
    def get_itemQty(self):
        itemQty = self.cart
        return itemQty

