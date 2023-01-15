a = int(input('ketik angka : '))

listpri = ['bulat', 'cacah', 'asli', 'genap', 'prima']
listkom = ['bulat', 'cacah', 'asli', 'ganjil', 'komposit']
listnol = ['nol']
listneg = ['negatif']

if ((a >= 0 or a <= 0)): #bulat
    if a >= 0: #cacah
        if a >= 1: #asli
            if a % 2 == 0: #genap
                if a > 1: #komposit
                    for i in range(2, a):
                        if (a % i) == 0:
                            print(listkom)
                            break
                    else: #prima
                        print(listpri)
                else:
                    print()
            else: #ganjil
                if a > 1: #komposit
                    for i in range(2, a):
                        if (a % i) == 0:
                            print(listkom)
                            break
                    else: #prima
                        print(listpri)
                else:
                    print()
        elif a == 0: #bilangan nol
            print(listnol)
        else :
            print()
    else : #negatif
        print(listneg)
else :
    print()