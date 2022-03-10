class Tomato:
    states = {0:'None',1:'Flowering',2:'Green',3:'Red'}
    def __init__(self, index):
        self._index = index
        self._state = Tomato.states[0]

    def grow(self):
        for key in Tomato.states.keys():
            if Tomato.states[key] == self._state:
                if not(self.is_ripe()):
                    self._state = Tomato.states[key + 1]
                    break
                else:
                    self._state = Tomato.states[len(Tomato.states) - 1]
                    break

    def is_ripe(self):
        if self._state == Tomato.states[len(Tomato.states) - 1]: return True
        else: return False

class TomatoBash:
    def __init__(self, num_tomatos):
        self.tomatoes = {}
        for el in range(int(num_tomatos)):
            self.tomatoes[el] = Tomato(el)

    def grow_all(self):
        for num_bash in self.tomatoes.keys():
            self.tomatoes[num_bash].grow()

    def all_are_ripe(self):
        result = False
        for num_bash in self.tomatoes.keys():
            if self.tomatoes[num_bash].is_ripe():
                result = self.tomatoes[num_bash].is_ripe()
            else:
                result = self.tomatoes[num_bash].is_ripe()
                break
        return result

    def give_away_all(self):
        self.tomatoes = {}

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Gardener is working...')
        self._plant.grow_all()
        print('Gardener finished')

    def harvest(self):
        print('Gardener is harvesting...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Harvesting is finished')
        else:
            print('Too early! Your plant is green and not ripe.')

    @staticmethod
    def knowledge_base():
        print('''Harvest time for tomatoes should ideally occur
    when the fruit is a mature green and
    then allowed to ripen off the vine.
    This prevents splitting or bruising
    and allows for a measure of control over the ripening process.''')







if __name__=='__main__':
    Gardener.knowledge_base()
    tomatos = TomatoBash(5)
    people = Gardener('Egor',tomatos)
    people.work()
    people.work()
    people.work()
    people.harvest()
    







