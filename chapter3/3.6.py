a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
if((a>0) and (b>0) and(c>0)):
    if(a==b==c):
        print('tam giac deu')
    elif(a*a==b*b+c*c) or (b*b==a*a+c*c) or (c*c==b*b+a*a):
        print('tam giac vuong')
    else:
        print('tam giac loai khac')
else:
    print('khong hop le')