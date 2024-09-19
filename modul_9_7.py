def is_prime(func):
    def wrapper(*nums):
        calc_result = func(*nums)
        for i in range(2, calc_result):
            prime = True
            if calc_result == 1:
                continue
            for j in range(2, i):
                if calc_result % j == 0:
                    prime = False
        if prime == True:
            print('Простое')
        else:
            print('Составное')
        return calc_result
    return wrapper


@is_prime
def sum_three(*num):
    r = sum(num)
    return r

result = sum_three(1745,1,1)
print(result)
