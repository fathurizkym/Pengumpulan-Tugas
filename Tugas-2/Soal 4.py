if __name__ == '__main__':
    #Nomor 4
    num = int(input('Enter the Nth Fibonacci number you wish to calculate or QUIT to quit: '))
    a = 0
    b = 1
    if num <= 0:
        print('The Output of your input is ' , a)
    else:
        print(a, b, end=" ")
        for i in range(2 , num):
            c = a + b
            print(c, end=" ")
            a = b
            b = c