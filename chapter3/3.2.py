a=float(input('M1='))
b=float(input('M2='))
c=float(input('M3='))
P=float(input('S='))
Phaitra=int(input("S="))
if P<=100:
    Phaitra=P*a
elif P>101 and P<=150:
    Phaitra=(P-100)*b+100*a
else:
    P>150
    Phaitra=(P-150)*c+50*b+100*a
print('Phai tra=', Phaitra)