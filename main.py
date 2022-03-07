import human
import house

if __name__=='__main__':
    human.Human.default_info()
    vasya = human.Human('Vasya',23)
    vasya.info()

    sm_house = house.Small_House(12_000)

    vasya.buy_house(sm_house,5)
    vasya.earn_money(15_000)
    vasya.buy_house(sm_house,5)
    vasya.info()