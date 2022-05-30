#Product
from itertools import product
a = [1, 3]
b = [2, 4]
prod = product(a,b)
print(prod)                         
print(list(prod))

a = [1, 3]
b = [2, 4]
prod = product(a,b, repeat=2)
print(prod)                         
print(list(prod))


#permutation
from itertools import permutations

a = [1,2,3]
perm = permutations(a)
print(perm)                                 
print(list(perm))

a = [1,2,3]
perm = permutations(a, 2)
print(perm)                                
print(list(perm))


#combination
from itertools import combinations , combinations_with_replacement

a = [1,2,3,4]
comb = combinations(a, 2)                     
print(comb)                                  
print(list(comb))
#with repetation
a = [1,2,3,4]
comb1 = combinations_with_replacement(a, 2)                     
print(comb1)                                  
print(list(comb1))


#accumulate
from itertools import accumulate

a = [1,2,3,4]
acc = accumulate(a)
print(acc)                                    
print(a)
print(list(acc))                              


#multiplying the list
from itertools import accumulate
import operator

a = [1,2,3,4]
acc = accumulate(a, func= operator.mul)
print(acc)                                    
print(a)
print(list(acc))                            

#maximize the list
from itertools import accumulate
a = [1,2,5,6,8,3,4]
acc = accumulate(a, func= max)
print(acc)                                    
print(a)
print(list(acc))



#groupby
from itertools import groupby

a = [1,2,3,4]

def smaller_than_2(x):
    return x < 2
group_obj = groupby(a, key = smaller_than_2 )
print(group_obj)                                  

for key, value in group_obj:                             
    print(key, list(value))

#using lambda
a = [1,2,3,4]
group_obj = groupby(a, key = lambda x: x < 2 )
print(group_obj)                                  

for key, value in group_obj:                            
    print(key, list(value))

