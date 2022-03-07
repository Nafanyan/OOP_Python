import house

class Human:
    # static field
    default_name = 'No name'
    default_age = 0
    def __init__(self,name=default_name,age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None
    def info(self):
        print(f'Name: {self.name}\n'
              f'Age: {self.age}\n'
              f'Money: {self.__money}\n'
              f'House: {self.__house}\n')
    @staticmethod
    def default_info():
        print(f'Default name: {Human.default_name}\n'
              f'Default age: {Human.default_age}\n')

    def buy_house(self, house, discount):
        final_price = house.final_price(discount)
        if self.__money < final_price: print('Недостаточно средств\n')
        else:
            self.__make_deal(house,final_price)
            print(f'Куплен дом по цене {final_price}\nОсталось: {self.__money}')

    def earn_money(self,money):
        self.__money += money
        print(f'Заработали {self.__money}\n')

    def __make_deal(self,house,price):
        self.__money -= price
        self.__house = house




