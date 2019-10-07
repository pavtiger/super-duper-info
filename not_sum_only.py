import numpy

def not_sum_only(*args, mode = 'sum'):
    if mode == 'sum':
        sum = 0
        for num in args:
            sum += num
        return sum
    
    elif mode == 'mult':
        mult = 1
        for num in args:
            mult = mult * num
        return mult
    
    elif mode == 'average':
        sum = 0
        for num in args:
            sum += num
        return sum / len(args)
    
    elif mode == 'sdev':
        return numpy.std(args)
    
    else:
        raise Exception('invalid mode')
    
#print(not_sum_only(1, 2, 3, mode = 'sdev'))
