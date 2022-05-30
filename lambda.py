add = lambda x : x + 15
print(add(15))

mult = lambda a,b : a*b
print(mult(5,9))

point2D = [(1,2), (5,-1), (8,-5), (3,2)]
point2D_sort = sorted(point2D)
print(point2D)
print(point2D_sort)                           
point2D = [(1,2), (5,-1), (8,-5), (3,2)]
point2D_sort = sorted(point2D, key = lambda x : x[1])
print(point2D_sort)
