import random

#random float in [0,1]
a = random.random()
print(a)

# random float in range [a,b]
a = random.uniform(1 , 10)
print(a)

# random integer in range [a,b] where b is included
a = random.randint(1,5)
print(a)

# random integer in range [a,b) where b is excluded
a = random.randrange(1,6)
print(a)

# random float from a normal distribution with mu and sigma
a = random.normalvariate(0, 1)
print(a)

# choose a random element from a sequence
a = random.choice(list("ABCDEFGHI"))
print(a)

# choose unique random elements from a sequence
a = random.sample(list("ABCDEFGHI"), 3)
print(a)

# choose k elements with replacement, and return k sized list
a = random.choices(list("ABCDEFGHI"),k=3)
print(a)

# shuffle list in place
a = list("ABCDEFGHI")
random.shuffle(a)
print(a)

#seeding

random.seed(1)
print(random.random())

random.seed(42) 
print(random.random())

random.seed(1)
print(random.random())

random.seed(42) 
print(random.random())

import secrets

# random integer in range [0, n).
a = secrets.randbelow(10)
print(a)

# return an integer with k random bits.
a = secrets.randbits(3)
print(a)

# choose a random element from a sequence
a = secrets.choice(list("ABCDEFGHI"))
print(a)

import numpy as np

print(np.random.rand(3,3))
print(np.random.randint(0,10,(3,4)))
print(np.random.randn(5))

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
np.random.shuffle(arr)
print(arr)