#QS01
i=1
while i <= 100:
    print(i)
    i+=1

#QS02
i = 100
while i >= 1:
    print(i)
    i-=1

#qs03
n = int (input("enter numbe: "))
i = 1
while i <= 10:
    print(n*i)
    i+=1

#qs04
nums = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

#qs05
nums = (1,4,9,16,25,36,49,64,81,100)
x = 36

i = 0
while i < len(nums):
    if(nums[i] ==x ):
        print("found at idx ", i)
    else :
        print("finding...")
    i += 1

