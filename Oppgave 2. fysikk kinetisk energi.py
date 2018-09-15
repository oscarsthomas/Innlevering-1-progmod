import math

def vfe():          # vekt fart energi (vfe) funksjon, får vite hvilken variabel som skal tas hensyn til 
    valg = 0
    while valg != 1 or valg != 2 or valg != 3:
        print('I fysikk så er formelen for kinetisk energi')
        print('E=1/2*m*v^2')
        print('E er energien målt i joule, m er massen til legemet i kg,')
        print('og v er farten til legemet i m/s')
        print('Skal du regne ut E, m, eller v?')
        valg = input('1 for E, 2 for m, 3 for v: ')
        
        return valg
    
    
def regnE():        # Regner formelen som blir vist hos vfe på hensyn til E
    m = float(input('Hva er massen i kg til legemet? '))
    v = float(input('Hva er farten i m/s til legemet? '))
    e = (1/2)*m*v**2
    print('E =', e,'J')
    
    
def regnM():        # Regner formelen som blir vist hos vfe på hensyn til m
    e = float(input('Hva er energien i joule til legemet? '))
    v = float(input('Hva er farten i m/s til legemet? '))
    m = (2*e)/(v**2)
    print('m =', m,'Kg')
    
def regnV():        # Regner formelen som blir vist hos vfe på hensyn til v
    e = float(input('Hva er energien i joule til legemet? '))
    m = float(input('Hva er massen i kg til legemet? '))
    v = math.sqrt((2*e)/m)
    print('v =', v,'m/s')
    
    
    
    
nyTest = 'ja'
while nyTest == 'ja' or nyTest == 'j':
    x = vfe()       # Lagrer hvilken variabel som skal tas hensyn til i variablen x, og videre ser om det er e, f, v
    if x == '1':
        regnE()
    elif x == '2':
        regnM()
    elif x == '3':
        regnV()
    else:
        print(x, 'er ikke et svar alternativ.')
    
    nyTest = input('Ønsker du å gjøre testen på nytt? (ja eller j for en ny test): ')