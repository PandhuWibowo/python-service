import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import get_root_message, calculate_addition

def test_root():
    result = get_root_message()
    assert result == {"message": "Hello World"}

def test_addition():
    result = calculate_addition(5, 7)
    assert result == {"result": 12}

    result = calculate_addition(-3, 8)
    assert result == {"result": 5}
