from math import lcm
from math import gcd

a = (int(input('ketik angka pertama           : ')))
b = (int(input('ketik angka kedua             : ')))

y = (lcm(a, b))
x = (gcd(a, b))
print('FPB dari angka ' + str(a) + ' dan ' + str(b) + " adalah : " + str(x) )
print('KPK dari angka ' + str(a) + ' dan ' + str(b) + " adalah : " + str(y) )

