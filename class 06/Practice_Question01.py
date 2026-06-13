def cals_sum(n):
    if( n == 0):
        return 0
    return cals_sum(n-1) + n
sum = cals_sum(10)
print(sum)