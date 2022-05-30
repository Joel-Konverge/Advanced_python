#counter
from collections import Counter

a="aaaaabbbcccc"
mycounter = Counter(a)
print(mycounter)
#items
print(mycounter.items())
#keys
print(mycounter.keys())
#values
print(mycounter.values())
#most common
print(mycounter.most_common(1))
print(mycounter.most_common(2))
print(mycounter.most_common(1)[0][0])
print(mycounter.elements())              
print(list(mycounter.elements()))
print("".join(list(mycounter.elements())))


#namedtuple
from collections import namedtuple
Point=namedtuple("Point" , "x,y")
pt=Point(1 , -6)
print(pt)
print(pt.x)
print(pt.y)


#ordereddict
from collections import OrderedDict

ordered_dict = OrderedDict()
ordered_dict ['b']=2
ordered_dict ['c']=3
ordered_dict ['d']=4
ordered_dict ['a']=1
print(ordered_dict)


#defaultdict
from collections import defaultdict

d = defaultdict(int)
d["a"] = 1
d["b"] = 2
print(d)
print(d["a"])
print(d["b"])
print(d["c"])

d = defaultdict(float)
d["a"] = 1
d["b"] = 2
print(d)
print(d["a"])
print(d["b"])
print(d["c"])


#deque
from collections import deque

d=deque()
#append
d.append(1)
d.append(2)
print(d)
#appending to the left side
d.appendleft(3)
print(d)
#popping
d.pop()
print(d)
#popping to the left side
d.popleft()
print(d)
#extend
d.extend([4,5,6])
print(d)
#extend to the left
d.extendleft([3,2,1])
print(d)
#rotate 
d.rotate(1)
print(d)
d.rotate(2)
print(d)
#rotate to the left
d.rotate(-1)
print(d)
d.rotate(-2)
print(d)
