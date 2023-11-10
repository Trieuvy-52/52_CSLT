a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if (a+b)>c and (a+c)>b and (b+c)>a:
    p=(a+b+c)/2
    S_tamgiac = (p*(p-a)*(p-b)*(p-c))**0.5
    print("Dien tich tam giac=", S_tamgiac)
else:
    print("Khong hop le")