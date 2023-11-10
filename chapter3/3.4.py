toan=float(input("Nhap diem mon toan: "))
ly=float(input("nhap diem mon ly: "))
hoa=float(input("nhap diem mon hoa: "))
trungbinh= (toan*2+ly*3+hoa)/6
print("Diem trung binh : ", trungbinh)
DTB=trungbinh
if (DTB < 3):
    print("Hoc luc kem")
elif (DTB >= 3 and DTB < 5):
    print("Hoc luc yeu")
elif (DTB >= 5 and DTB <6):
    print ("Hoc luc trung binh")
elif (DTB >=6 and DTB <7):
    print ("Hoc luc trung binh kha")
elif (DTB >=7 and DTB < 8):
    print ("Hoc luc kha")
elif (DTB >=8 and DTB < 9):
    print ("Hoc luc gioi")
else:
    (DTB >=9 and DTB < 10)
    print ("Hoc luc xuat sac")
    


