if __name__ == '__main__':
    #Soal 5
    
    import math
    JM = 120
    K1 = 60
    K2 = 40
    ta = 9

    T = (JM / (K1 + K2))
    TJam = math.floor(T) + ta
    TMnt = math.ceil((T - math.floor(T)) * 60)
    print( '''Diket   : Jarak Mobil A & B = 120 km
          Kecepatan mobil A =  60 km/jam
          Kecepatan mobil B =  40 km/jam
          A & B start pukul =   9 wib \nDitanya : Pukul berapa A & B bertabrakan?''')
    print(f'Jawab   : Mereka akan bertabrakan pada pukul {TJam} lewat {TMnt} menit')