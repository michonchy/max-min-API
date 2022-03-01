import json

import pytest

from max_min import app

def test_number_max_min():
    assert app.number_max_min([2,5,100]) == (100,2)
