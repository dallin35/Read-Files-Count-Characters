import os,sys
import pytest
from assignment import get_number_of_a
from assignment import get_number_of_z
from assignment import get_number_of_percent
from assignment import get_number_of_char

def check_if_file_exists():
    try:
        exists = os.path.exists("assignment.py")
        assert exists == True
    except:
        sys.exit()

def test_letter_a():
    # If your code is returning 26060 it is because your code is case sensitive
    assert get_number_of_a() == 4335184
def test_letter_z():
    # If your code is returning 9296 it is because your code is case sensitive
    assert get_number_of_z() == 130261
def test_char_percent():
    # If your code is returning 2276 it is because your code is case sensitive
    assert get_number_of_percent() == 1836 
def test_user_char_b():
    # If your code is returning 5335 it is because your code is case sensitive
    assert get_number_of_char("b") == 1023496
def test_user_char_tilde():
    # If your code is returning 5335 it is because your code is case sensitive
    assert get_number_of_char("~") == 963
