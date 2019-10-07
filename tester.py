from not_sum_only import *

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
    assert not_sum_only(-1, 0, -2, mode = 'average') == -1
    assert not_sum_only(0, 0, -21, mode = 'average') == -7

def test_sdev():
    check([1, 2, 3], 0.81649658092773)
    check([5, 2, 5], 1.4142135623731)
    check([3, 8, 3, 1, 62, 4, 1, 7, 3, 9, 2, 8, 3, 7, 3, 7, 3], 13.76219182672)
    check([-0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0, -0], 0)
    check([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1], 2.7499685216028)
    
def check(param, ans):
    assert not_sum_only(param, mode = 'sdev') >= ans - 0.001 <= ans + 0.001
