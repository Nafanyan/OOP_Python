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


if __name__=='__main__':
    print(Tomato.states)
    tom = Tomato(0)


