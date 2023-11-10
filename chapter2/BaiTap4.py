a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
import math
S=(a+b+c)/2
x=(S*(S-a)*(S-b)*(S-c))
T= math.sqrt(x)
print("Dien tich= ",T)