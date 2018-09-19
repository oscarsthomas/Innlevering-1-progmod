def intTest():      #Sjekker om tallet er int, om det er stÃ¸rre enn null, og gir feilmelding ellers.

    try:
        x = input('Gi meg et heltall som jeg skal ta fakulteten til: ')
        y = float(x)
        
        if y == int(y):
            b = int(y)
            
            if b < 0:
                print('Tallet er mindre enn null, og kan ikke brukes til fakultet')
            else:
                return b
        else:
            print('Det du skrev inn er ikke et heltall')
            
    except ValueError:
        print('Det du skrev inn gir ikke mening')
        
        
def fakultet(x):
    if x == 0:
        x = 1
        return x
    else: 
        for i in range(1,x):
            x = x*i
        
        return x
    

ny = 'ja'
while ny == 'ja' or ny == 'j':
    
    x = intTest()
    y = fakultet(x)
    print(y)
    
    
    
    ny = input('Ønsker du å ta en til test? (ja eller j for en ny test): ')