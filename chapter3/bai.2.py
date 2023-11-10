n=int(input("n="))
LaSoNT=1  #Biến cờ, có 2 trạng thái 0 và 1
#n là số NT nếu ko tồn tại một số từ 2-->(n-1) mà n chia hết
for i in range(2,n,1):
    if (n%i==0):   # n chia hết chi i--> n ko là SNT
        LaSoNT=0
        break
if (LaSoNT==1):
    print(n,"la SNT")
else:
    print(n,"khong la SNT")