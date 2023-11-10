n=int(input("Nhap gia tri: "))
giatri=1
if n<0:
   break
elif n==0 or n==1:
   print(giatri)
else:
   i=2
while i<=n:
   giatri*=i
   i+=1
print(giatri)

 
    


    