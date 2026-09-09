from collections import Counter
numbers=[1,2,2,2,2,3,3,4,5,5,5,6]
c=Counter(numbers)
print(c)
print(c[6])
######
from collections import defaultdict,UserDict
d=defaultdict(int)
d['Orange']+=1
d['Apple']+=1
d['Mango']+=1
d['Apple']+=1
print(d)
d=UserDict({'A':10,'B':1000,'C':100})
print(d)

#############
from typing import ChainMap
from collections import UserList,UserString
numbers=UserList([1,2,3])
numbers.append(4)
print(numbers)
s=UserString("Aishwarya")
print(s)

from collections import namedtuple 
student=namedtuple("Student",["name","age"])
s=student("Aishwarya",20)
print(s.name)
print(s.age)

D1={"A":10}
D2={"B":11}
D=ChainMap(D1,D2)
print(D["A"])
print(D["B"])

########
from collections import UserList,UserString
numbers=UserList([1,2,3])
numbers.append(4)
print(numbers)
s=UserString("Aishwarya")
print(s)

from collections import namedtuple 
student=namedtuple("Student",["name","age"])
s=student("Aishwarya",20)
print(s.name)
print(s.age)