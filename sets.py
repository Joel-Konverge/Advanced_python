myset={1,2,3}
print(myset)
print(type(myset))
myset=set([1,2,3,4])
print(myset)
myset=set("hello")
print(myset)
myset=set()

#to add
myset.add(1)
myset.add(2)
myset.add(3)
myset.add(4)
myset.add(5)
print(myset)

#to discard/remove
myset.remove(4)
print(myset)
myset.discard(3)
print(myset)
myset.pop()
print(myset)
myset.clear()
print(myset)

#union
o={1,3,5,7,9}
e={0,2,4,6,8}
p={2,3,5,7}
u=o.union(e)
print(u)

#intersection
i=o.intersection(e)
print(i)
i=o.intersection(p)
print(i)
i=e.intersection(p)
print(i)

#difference
setA={1,2,3,4,5,6,7,8,9}
setB={1,2,3,9,10,11,12,13,15,19}
diff=setA.difference(setB)
print(diff)
diff=setB.difference(setA)
print(diff)

#symmetric difference
symdiff=setA.symmetric_difference(setB)
print(symdiff) 
symdiff=setB.symmetric_difference(setA)
print(symdiff)

#update 
setA.update(setB)
print(setA)
setB.update(setA)
print(setB)

#intersection update
setA.intersection_update(setB)
print(setA)
setB.intersection_update(setA)
print(setB)

#difference update
setA.difference_update(setB)
print(setA)

#symmetric difference update
setA.symmetric_difference_update(setB)
print(setA)

# superset subset disjoin
setA={1,2,3,4,5,6,7,8,9}
setB={1,2,3,9}

#subset
print(setA.issubset(setB))
print(setB.issubset(setA))

#superset
print(setA.issuperset(setB))
print(setB.issuperset(setA))

#disjoin
print(setA.isdisjoint(setB))
print(setB.isdisjoint(setA))

