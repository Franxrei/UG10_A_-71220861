print("===== Selamat datang di Toko Andi Tersenyum, Selamat Belanja! =====")
total =int(input("Total Belanja :Rp. "))
total1 = total - (total/100)*2
total2 = total - (total1/100)*5
total3 = total - (total2/100)*10
if int(total)<100000 :
    print ("tidak ada diskon! maka yang anda bayarkan adalah :Rp.",total)
elif int(total)>=100000 :
    print ("biaya yang harus di bayarkan setelah diskon adalah :Rp.",total1)
elif int(total)>=500000 :
    print("biaya yang harus di bayarkan setelah diskon adalah :Rp.",total2)
elif int(total)>=1000000 :
    print("biaya yang harus di bayarkan setelah diskon adalah :Rp.",total3)
else :
    print("tidak belanja datang lagi")