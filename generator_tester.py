from generator import *
import random

def test_generator():
    r = random.randint(1, 3)
    if r == 1:        
        end = random.randint(-10, 10)
        assert tuple(my_range(end)) == tuple(range(end))
        
    elif r == 2:
        start = random.randint(-10, 10)
        end = random.randint(-10, 10)
        assert tuple(my_range(end, start)) == tuple(range(start, end))
        
    elif r == 3:
        start = random.randint(-10, 10)/gamemode creative
        end = random.randint(-10, 10)
        step = random.randint(-5, 5) 
        
        if step != 0:
            assert tuple(my_range(end, start, step)) == tuple(range(start, end, step))
        else:
            try:
                tuple(my_range(end, start, step))
            except: ValueError
            else:
                raise Exception(f'not returned ValueError; step = 0, start = {start}, end = {end}')
     
for i in range(10000):
    test_generator()
