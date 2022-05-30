def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num = num -  1

cd = countdown(3)
print(next(cd))
print(next(cd))
print(next(cd))
#will through error if next is called again

cd = countdown(3)
sum_cd = sum(cd)
print(sum_cd)

cd = countdown(3)
sorted_cd = sorted(cd)
print(sorted_cd)

#comparision between list and generator
#list
def firstn(n):
    num = 0
    nums = []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
import sys
print(sys.getsizeof(firstn(1000000)))

#generator
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
import sys
print(sys.getsizeof(firstn(1000000)))

# generator expression
mygenerator = (i for i in range(1000) if i % 2 == 0)
print(sys.getsizeof(mygenerator), "bytes")

# list comprehension
mylist = [i for i in range(1000) if i % 2 == 0]
print(sys.getsizeof(mylist), "bytes")
