
def print_faktor(x):
    loop = 2
    _tmp = []
    while loop <= x:
        if x % loop == 0:
            x/=loop
            _tmp.append(loop)
        else:
            loop+=1
    return _tmp

    
num = int(input("Masukkan bilangan: "))
a = print_faktor(num)
print a