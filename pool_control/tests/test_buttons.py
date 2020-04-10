import pytest
from buttons.buttons import *


def test_buttons_are_off():
    button = Buttons('pump')
    assert button.button_state() == 'off'


def test_buttons_are_on():
    button = Buttons('pump')
    button.set_button_state('on')
    assert button.button_state() == 'on'


def test_spa_button():
    button = SpaPoolButton()
    assert button.button_state() == 'off'


def test_spa_button_pool():
    button = SpaPoolButton()
    button.set_button_state('pool')
    assert button.button_state() == 'pool'


def test_spa_button_sap():
    button = SpaPoolButton()
    button.set_button_state('spa')
    assert button.button_state() == 'spa'


def test_spa_button_set_raise():
    button = SpaPoolButton()
    with pytest.raises(ValueError):
        button.set_button_state('stuff')
