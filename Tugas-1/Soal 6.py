if __name__ == '__main__':
    #Soal 6
    
    print('Harga apel   = Rp,10.000')
    print('Harga jeruk  = Rp,15.000')
    print('Harga anggur = Rp,20.000')

    apel   = input('Masukan jumlah apel   : ')
    jeruk  = input('Masukan jumlah Jeruk  : ')
    anggur = input('Masukan jumlah Anggur : ')

    H_apel   = int(apel)   * 10000
    H_jeruk  = int(jeruk)  * 15000
    H_anggur = int(anggur) * 20000

    print(f'Anda membeli apel sebanyak {apel} dengan harga Rp,{H_apel}')
    print(f'Anda membeli apel sebanyak {jeruk} dengan harga Rp,{H_jeruk}')
    print(f'Anda membeli apel sebanyak {anggur} dengan harga Rp,{H_anggur}')