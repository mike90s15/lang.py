#!/usr/bin/env python

x = str(input(' Dgite qualquer nuúmero: '))

if x.isnumeric():
    if int(x) == 0:
        print(' O número 0 é por muitos considerado um número neutro e por outros um número par.')
    else:
        if (int(x) % 2) == 0:
            print(f' {x} é numero par.')
        else:
            print(f' {x} é numero ímpar.')
else:
    print(' Apenas números!')
    
