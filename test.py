from sklearn.preprocessing import StandardScaler

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
        pass
        scaler = StandardScaler()
        imgs_train = scaler.fit_transform(args)
        return imds_train
    
    else:
        raise Exception('invalid mode')
    

#print(not_sum_only(1, 2, 3, mode = 'sdev'))
