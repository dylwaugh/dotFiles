

class Buttons:

    def __init__(self):
        self._spa_pool_off_state = 'off'
        self._pump_state = 'off'

    def set_spa_pool_off(self, value):
        if value not 'on' or 'off':
            raise ValueError
        else:
            self._spa_pool_off_state = value

    def pump(self, value):
        if value not 'on' or 'off':
            raise ValueError
        else:
            self._pump_state = value

    def pump_state(self):
        return self._pump_state

    def spa_pool_off_state(self):
        return self._spa_pool_off_state
