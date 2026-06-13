'''cities = ["Mumbai", "Delhi", "Lucknow", "Kolkata", "chennai", "Varanshi"]
heroes = ["Ironman", "Thor", "Loki", "Suparman", "Spiderman", "Thainos"]

def print_len(list):
    print(len(list))

def print_len(list):
    for item in list:
        print(item, end=" ")

print_len(heroes)
print
'''

'''def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(22)'''

def converter(usd_val):
    inr_val= usd_val*95
    print(usd_val, "USD =", inr_val, "INR ")
    
converter(37)