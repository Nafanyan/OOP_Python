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
        pass

    def earn_money(self,money):
        self.__money += money
        print(f'Заработали {self.__money}')

    def __make_deal(self,house,price):
        self.__money -= price
        self.__house = house



if __name__=='__main__':
    print(Human.default_name,Human.default_age)
    petr = Human('Fedr',19)
    petr.info()
    petr.earn_money(1000)
    petr.info()
