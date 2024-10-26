# Program Mencari Bilangan Terbesar
Program ini adalah skrip sederhana dalam bahasa Python yang menentukan bilangan terbesar di
antara tiga bilangan yang dimasukkan oleh pengguna. 

## Deskripsi Program 
Program ini dibuat menggunakan bahasa python dengan fitur: 

- Input dari pengguna dengan tipe data integer.
- Logika perbandingan untuk menentukan bilangan terbesar.
- Validasi input agar pengguna memasukkan bilangan yang sesuai.

## Flowchart Program 
![Flowchart1](Flowchart1.png)

## Kode Program 
``` Python
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
```

# Output Program 
````
masukan bilangan A: 2002
masukan bilangan B:1999
masukan bilangan C:2004
bilangan terbesar adalah: 2004.0
````

# Cara Kerja Program 



