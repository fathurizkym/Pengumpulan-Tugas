if __name__ == '__main__':
    #Nomor 1
    upTo = int(input('Masukan angka : '))
    kond = '1. '
    for i in range(1 , upTo + 1):
        if(i % 3 == 0) and (i % 5 == 0):
            kond += 'FizzBuzz '
        elif (i % 3 == 0):
            kond += 'Fizz '
        elif(i % 5 == 0):
            kond += 'Buzz '
        else:
            kond += f'{str(i)} '
print(kond)