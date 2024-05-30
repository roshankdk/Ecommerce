class Cart():
    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get('session_key')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart
    
    def add(self,product):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'price':str(product.price)}
        
        self.session.modified = True
    
    def __len__(self):
        return len(self.cart)
