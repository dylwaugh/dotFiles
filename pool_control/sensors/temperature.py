import os
from pathlib import Path


class Temperature:
    ''' The clase to read the temperature sensor '''

    _temperature_file_value = 0
    _sensor = 0
    _set_value = 88 # our default highest temp

    def __init__(self, temp_file=None):
        # read temperature from sensor
        self._sensor = 5 # replace with ADC on pi
        #self._temperature_file_value = Path('/var/log/sensor').open()
        self.set_temperature_value(self._temperature_file_value)

    def set_temperature_value(self, value):
        self._set_value = value

    def get_set_temperature_value(self):
        return self._set_value

    def at_temperature(self):
        read_value = self.read_sensor_value()
        return self._set_value >= read_value

    @staticmethod
    def read_sensor_value():
        return 5
