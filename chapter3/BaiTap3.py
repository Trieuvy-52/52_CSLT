a = float(input("Tieu thu="))
thanhtien=a
if (a>=1 and a<=100):
    thanhtien*=550
    thanhtien+=(thanhtien*1.1)
    print("Phai tra=",thanhtien)
elif (a>=101 and a<=150):
    thanhtien*=750
    thanhtien+=(thanhtien*1.1)
    print("Phai tra=",thanhtien)
elif (a>=151 and a<=200):
    thanhtien*=950
    thanhtien+=(thanhtien*1.1)
    print("Phai tra=",thanhtien)
else:
    thanhtien*=1350
    thanhtien+=(thanhtien*1.1)
    print("Phai tra=",thanhtien)