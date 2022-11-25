nama = input('Masukan Nama Mahasiswa : ')
nim = input('Masukan Nim-Nya : ')
if nim[0:2]=='71'and int(nim[2:4])<=22 and int(nim[2:4])>=20:
    print(nama,'merupakan mahasiswa informatika angkatan 20 hingga 22')
else :
    print(nama, 'bukan mahasiswa informatika angkatan 20 hingga 22')  
