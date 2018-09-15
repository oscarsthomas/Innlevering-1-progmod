import math

def tall():             # Finner konsentrasjonen av H+ ioner i løsningen
    
    sjekk = 'nei'
    while sjekk == 'nei' or sjekk == 'n':
        print('Hvor mange H+ ioner har du i mol per liter? x*10^y')
        print()
        a = float(input('Hva er x verdien? '))
        b = float(input('Hva er y verdien? '))
        x = a*10**b
        print('Tallet du skrev inn er',a,'*10^',b,'. Det samme som',x)
        
        return x
        
def ph(y):              # Skriver ut hva slags type løsning det er
    if 0 < y < 7:
        print('Ph verdien er', y,'Ph, og blandingen er sur')
    elif y == 7:
        print('Ph verdien er', y,'Ph og blandingen er nøytral')
    elif 7 < y < 14:
        print('Ph verdien er', y,'Ph og blandingen er basisk')
    else:
        print('Ph verdien er enten under 0 eller over 14 som ikke går')
    
    
    
nyTest = 'ja'
while nyTest == 'ja' or nyTest == 'j':
    x = tall()
    y = -math.log10(x)      # Finner Ph verdien til løsningen
    print()
    ph(y)
    nyTest = input('Har du en ny løsning du vil vite Ph-en til? (ja eller j for en ny test): ')