class Cart():
    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session'] = {}

        self.cart = cart
    
    def add(self,product):
        product_id = str(product.id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price':str(product.price)}
        
        self.session.modified = True
