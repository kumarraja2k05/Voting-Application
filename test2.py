import math
import datetime
from pytest import MonkeyPatch
import unittest
from mock import MagicMock
import os

def test1():
    dob="2000-06-18"
    age=int(get_age(dob))
    assert age == 22


def test2():
    dob="2000-10-05"
    age=int(get_age(dob))
    assert age == 21

def test3():
    dob="2001-08-27"
    age=int(get_age(dob))
    assert age == 21
    
def get_age(dob):
        today = datetime.datetime.today()
        dob = str(dob)
        dob = datetime.datetime.strptime(dob, '%Y-%m-%d')
        age = str((today-dob)/365).split(" ")[0]
        return age
    
def mock_test():
    mock_file=MagicMock()
    mock_file.readLine=MagicMock(return_values="test line")
    mock_open=MagicMock(return_value=mock_file)
    # MonkeyPatch.setattr("builtins.open",,mock_open)
    MonkeyPatch.setattr(os, 'builtins.open', mock_open)
    dob="2001-08-27"
    result=int(get_age(dob))
    mock_open.assert_called_once_with(dob)
    
    # def mock_getcwd():
    #     return '/data/user/directory123'

    # monkeypatch.setattr(os, 'getcwd', mock_getcwd)
    # assert example1() == '/data/user/directory123'
    # mock_exists=MagicMock(return_value=False)
    # monkeypatch.setattr("os.path.exists",mock_exists)
    assert result==21
    

test1()
test2()
test3()
print()
mock_test()

