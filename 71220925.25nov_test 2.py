print(("=====selamat datang di Toko Andi Tersenyum, selamat belanja! ====="))
total = int(input("Total belanja : Rp."))


if total>=1000000:
    print(f'Biaya yang harus dibayar setlah diskon adalah : Rp.{total- (0.1*total)}')
if total >=500000:
     print(f'Biaya yang harus dibayar setelah diskon adalah : Rp.{total - (0.05*total)}')
elif total <100000:
     print(f'Tidak ada diskon! Maka yang anda bayarkan adalah : Rp.{total}')
elif total >=100000:
    print(f'Biaya yang harus dibayar setelah diskon adalag : Rp.{ total - (0.02*total)}')
    
