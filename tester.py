from test import *

def test_sum():
    assert not_sum_only(1, 2, 3, mode = 'sum') == 6
    assert not_sum_only(5, 2, 5, mode = 'sum') == 12
    assert not_sum_only(3, 8, 3, mode = 'sum') == 14
    assert not_sum_only(6, 9, 0, mode = 'sum') == 15
    assert not_sum_only(3, 5, 6, mode = 'sum') == 14
    assert not_sum_only(0, mode = 'sum') == 0
    assert not_sum_only(6, 0, -1, mode = 'sum') == 5
    
def test_mult():
    assert not_sum_only(1, 2, 3, mode = 'mult') == 6
    assert not_sum_only(5, 2, 5, mode = 'mult') == 50
    assert not_sum_only(3, 8, 3, mode = 'mult') == 72
    assert not_sum_only(6, 9, 0, mode = 'mult') == 0
    assert not_sum_only(3, 5, 6, mode = 'mult') == 90
    
def test_avg():
    assert not_sum_only(1, 2, 3, mode = 'average') == 2
    assert not_sum_only(5, 2, 5, mode = 'average') == 4
    assert not_sum_only(-5, -2, -5, mode = 'average') == -4
    assert not_sum_only(0, 0, 0, mode = 'average') == 0
    assert not_sum_only(-1, 0, -1, mode = 'average') == 0
    assert not_sum_only(0, 0, -1, mode = 'average') == 0.5

'''def test_sdev():
    assert not_sum_only(1, 2, 3, mode = 'sdev') == 6
    assert not_sum_only(5, 2, 5, mode = 'sdev') == 12
    assert not_sum_only(3, 8, 3, mode = 'sdev') == 14
    assert not_sum_only(6, 9, 0, mode = 'sdev') == 15
    assert not_sum_only(3, 5, 6, mode = 'sdev') == 14'''
