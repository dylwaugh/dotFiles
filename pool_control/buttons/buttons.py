
onoff = ('on', 'off')
spapooloff = ('spa', 'pool', 'off')

class Buttons:

    def __init__(self, name, state='off'):
        self._name = name
        self._button_state = state

    def set_button_state(self, value):
        if value not in onoff:
            raise ValueError
        else:
            self._button_state = value

    def button_state(self):
        return self._button_state


class SpaPoolButton(Buttons):

    def __init__(self, name):
        if name != 'spa_pool':
            raise ValueError
        super().__init__(name)

    def set_button_state(self, value):
        if value not in spapooloff:
            raise ValueError
        else:
            self._button_state = value