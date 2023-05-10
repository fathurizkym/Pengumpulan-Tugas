if __name__ == '__main__':
    #Soal 4
    
    jumlah = 49
    andi   = 4
    budi   = 10

    U_andi = andi/(andi+budi) * jumlah + 2
    U_budi = budi/(andi+budi) * jumlah + 2

    print( '''Diket   : Jumlah usia Andi & Budi = 49thn
          Rasio usia Andi & Budi  =  0.4 \nDitanya : Berapa usia Andi & Budi 2 tahun lagi?''')
    print(f'Usia Andi adalah : {U_andi}')
    print(f'Usia Budi adalah : {U_budi}')