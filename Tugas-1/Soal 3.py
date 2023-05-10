if __name__ == '__main__':
    #Soal 3
    
    x = 485
    _1Tahun = 360
    _1Bulan = 30
    _1Minggu = 7

    HThn  = x // _1Tahun
    HBln  = (x % _1Tahun) // _1Bulan
    HMggu = (x % _1Tahun) % _1Bulan // _1Minggu
    HHri  = ((x % _1Tahun) % _1Bulan % _1Minggu)

    print( '''Diket   : Jumlah hari = 485 hari \nDitanya : Nyatakan dalam tahun, bulan, minggu, dan hari''')
    print(f'Jawaba  : {HThn} Tahun {HBln} Bulan {HMggu} Minggu {HHri} Hari')


