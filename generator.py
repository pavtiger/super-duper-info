def my_range(end=0, start=0, step=1):
    i = start
    if step < 0:
        while i > end:
            yield i
            i += step
    elif step > 0:
        while i < end:
            yield i
            i += step
    else:
        raise ValueError

        
'''for x in my_range(20, 10, 2):
    print(x)'''
