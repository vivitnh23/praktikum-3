# input bilangan A, B, C
A = float(input("masukan bilangan A: "))
B = float(input("masukan bilangan B:"))
C = float(input("masukan bilangan C:"))

if A > B:
    if A > C:
        terbesar = A
    else:
        terbesar = C
else: 
    if B > C: 
        terbesar = B 
    else: 
        terbesar = C

print("bilangan terbesar adalah:" ,terbesar)
