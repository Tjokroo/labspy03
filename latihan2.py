print("Menampilkan bilangan terbesar dari n data yang di inputkan")

max = 0
while True:
    a = int(input("Masukan bilangan:"))
    if max < a :
        max = a
    if a == 0:
        break
print(max,"Merupakan bilangan terbesar")
