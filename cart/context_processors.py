from .cart import Cart

#creating the context processor 
def cart(request):
    # return the default data from our cart
    return {'carts': Cart(request)}