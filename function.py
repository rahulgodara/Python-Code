def decrement(num):
    while num>0 :
        print(num)
        num-=1


decrement(5)

print()

def decre(num):
    if num==0:
        return
    
    print(num)
    decre(num-1)


decre(5)


def recursive_sum(num):
    if num==0:
        return 0
    
    result = num + recursive_sum(num-1)
    return result

print(recursive_sum(10))

def fibonacci(num, fibo_series):
    if num<2:
        return
    l = len(fibo_series)
    new_num = fibo_series[l - 1] + fibo_series[l - 2]
    fibo_series.append(new_num)
    print("Series so far:", fibo_series)
    fibonacci(num-1, fibo_series)

series = [1,2]
fibonacci(10, series)
print(series)
