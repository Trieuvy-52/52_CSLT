n = int(input("Nhập số nguyên n: "))
str_n = ""
while n > 0:
    digit = n % 10
    str_n = ALPHABET[digit] + str_n
    n = n // 10
str_n = str_n[::-1]
str_n = ma_hoa_so_nguyen(n)
print("Chuỗi ký tự đã được mã hóa:", str_n)
    