a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
if((a>b and a>c) and (a !=b and a!= c)):
    print("SLN=",a)
elif((b>a and b>c)and (b !=a and b !=c)):
    print("SLN=",b)
elif((c>a and c>b) and (c!=a and c !=b)):
    print("SLN=",c)
else:
    print("SLN=7.0")
if((a<b and a<c) and (a !=b and a !=c)):
    print("SLN=7.0")
if((a<b and a<c) and (a != b and a != c)):
    print("SBN=",a)
elif((b<a and b<c) and (b != a and b != c)):
    print("SBN=",b)
elif((c<a and c<b) and (b != a and b != c)):
    print("SBN=",c)
else: 
    print("SBN=4.5")
