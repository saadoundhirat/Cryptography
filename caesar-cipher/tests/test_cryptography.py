import pytest
from caesar_cipher.caesar_cipher import *


def test_encrypt():
    expected = 'Wi xkwo sc Ckknyex Nrsbkd'
    actual = encrypt('My name is Saadoun Dhirat', 10)
    assert actual == expected

def test_decrypt():
    expected = 'My name is Saadoun Dhirat'
    actual = decrypt('Wi xkwo sc Ckknyex Nrsbkd', 10)
    assert actual == expected


def test_crack():
    assert crack('Wi xkwo sc Ckknyex Nrsbkd') == 'My name is Saadoun Dhirat'