n=int(input("n="))
gt=1
for i in range(1,n+1,1):     #i=(1,2,3,4,5,...,n)
    gt=gt*i
print(n,"!=",gt,sep="")