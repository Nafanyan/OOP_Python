class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price
    def final_price(self,discount):
        final_price = self._price - self._price / 100 * discount
        print(f'Final price: {final_price}')
        return final_price

class Small_House(House):
    default_area = 40
    def __init__(self,price):
        super().__init__(Small_House.default_area,price)
