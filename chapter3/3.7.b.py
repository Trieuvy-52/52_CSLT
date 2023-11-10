n = int(input("Nhập số nguyên n: "))
giai_thua = 1
for i in range(1, n + 1):
    giai_thua *= i
print("Giai thừa của n là:", giai_thua)

n = int(input("Nhập số nguyên n: "))
while n >= 0:
    giai_thua *= n
    n -= 1
    print("Giai thừa của n là:", giai_thua)
    n = int(input("Nhập số nguyên n: "))
    
    
