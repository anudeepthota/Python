def multi_param(*args):
    result = 1
    for x in args:
        result = result * x
        print(result)
    return result

multi_param(1, 2 , 3 , 5)