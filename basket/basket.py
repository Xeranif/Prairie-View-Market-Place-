
class Basket():
    """
    Base basket class
    """

    def __init__(self, request):

        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {'number':141414}
        self.basket = basket
        
    def add(self, product):
        """
        updates user basket session data
        """
        product_id = product.id

        if product_id not in self.basket:
            self.basket[product_id] = {'price': str(product.price)}

        self.session.modified = True
