# Program Mencari Bilangan Terbesar
Program ini adalah skrip sederhana dalam bahasa Python yang menentukan bilangan terbesar di
antara tiga bilangan yang dimasukkan oleh pengguna. 

## Deskripsi Program 
Program ini dibuat menggunakan bahasa python dengan fitur: 

- Input dari pengguna dengan tipe data integer.
- Logika perbandingan untuk menentukan bilangan terbesar.
- Validasi input agar pengguna memasukkan bilangan yang sesuai.

## Flowchart Program 
![Flowchart1](https://github.com/vivitnh23/praktikum-3/blob/main/Flowchart%201.png?raw=true)

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
Program ini dimulai dengan meminta pengguna menginput tiga angka. setelah menginput ketiga angka tersebut program menggunakan
fungsi IF/ELSE untuk menentukan angka yang paling besar diantara ketiga angka yang sudah diinputkan tadi. fungsi IF secara langsung membandingkan semua angka dan memilih angka terbesar untuk dicetak terakhir kali dan menampilkan kalimat yang lebih jelas. dengan 
menggunakan if/else membuat program lebih ringkas dan mudah dipahami. dengan melakukan pengecekan dengan urutan :

- apakah A>B ?
- jika ya : cek apakah A>C?
- jika Ya: A adalah yang terbesar
- jika tidak : C adalah terbesar
- jika tidak : cek apakah B>C ?
- jika ya : B adalah yang terbesar
- jika tidak : C adalah nilai terbesar   


