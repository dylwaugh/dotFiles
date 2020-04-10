from transitions import Machine
from transitions.extensions import GraphMachine as GMachine
from sensors.temperature import *
from buttons.buttons import *

class HeaterControl(object):

    # Define some states: off - heater is off
    #                     waiting - pool is at temperature
    #                     heating - pool is cold and heater is on
    states = ['off', 'waiting', 'heating']

    def __init__(self, custom_temperature=None, custom_button=None):

        # we need to know the temperature or set the set_temperature. Use our class for that
        self.temp = custom_temperature or Temperature()

        # What state is the pool/spa/off button in?
        self.pump_button = custom_button or Buttons('pump')
        self.spa_button = SpaPoolButton()

        # What states is the pump in?
        self.pump_state = 'off'

        # What states is the heater in? # 'spa' or 'pool' or 'off'
        self.heater_state = 'off'

        # Initialize the state machine
        self.machine = Machine(model=self, states=HeaterControl.states, initial='off')

        # Add some transitions. We could also define these using a static list of
        # dictionaries, as we did with states above, and then pass the list to
        # the Machine initializer as the transitions= argument.

        # Someone wants to heat the pool
        self.machine.add_transition(trigger='button_press', source='off', dest='waiting')

        # Someone wants to turn off the heat
        self.machine.add_transition(trigger='button_press', source='waiting', dest='off')

        # The pool is cold, turn the heat on
        self.machine.add_transition(trigger='temperature', source='waiting', dest='heating')

        # The pool is hot or at temp
        self.machine.add_transition(trigger='temperature_set', source='heating', dest='waiting')

        # Someone wants to turn off the heat
        self.machine.add_transition(trigger='button_press', source='heating', dest='off')

if __name__ == "__main__":
    m = HeaterControl()
    # without further arguments pygraphviz will be used
    gmachine = GMachine(model=m)

    # draw the whole graph ...
    m.get_graph().draw('my_state_diagram.png', prog='dot')
