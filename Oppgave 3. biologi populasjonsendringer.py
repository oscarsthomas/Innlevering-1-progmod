def intro():        # Introduksjon som også finner ut om bestandne øker eller minker
    print('Nå skal jeg hjelpe deg med å beregne hvor mange dyr du har')
    print('når jeg får vite hvor mange som er i bestanden i dag, om bestanden synker eller øker i prosent')
    print('og i hvor mange år bestanden endres.')
    print('Så først. Øker eller minker bestanden?')
    x = input('1 = bestanden øker, og 2 = bestanden minker: ')
    
    return x

def bøker():        # bøker = bestanden øker, får vite bestand, prosent og antall år, når bestanden øker. Finner hva bestanden er etter å år
    b = float(input('Hvor mange individer består bestanden av nå? '))
    p = float(input('Hvor mange prosent vokser bestanden med for hvert år? '))
    å = int(input('Etter hvor mange år ønsker du å se hvor mye bestanden har økt? '))
    for i in range(0,å+1):
        n = b*(1+p/100)**i
    
    print()
    print('Bestanden består av', n,'individer etter', å,'år')
    
def bminker():      # bminker = bestanden minker, får vite bestand, prosen og antall år, når bestanden minker. Finner hva bestanden er etter å år
    b = float(input('Hvor mange individer består bestanden av nå? '))
    p = float(input('Hvor mange prosent minker bestanden med for hvert år? '))
    å = int(input('Etter hvor mange år ønsker du å se hvor mye bestanden har minket? '))
    for i in range(0,å+1):
        n = b*(1-p/100)**i
    
    print()
    print('Bestanden består av', n,'individer etter', å,'år')
    


nyTest = 'ja'
while nyTest == 'ja' or nyTest == 'j':      #Brukes for å se om vi skal ta testen igjen
    x = intro()                             #Sier at valget fra intro() skal lagres i variablen x
    if x == '1':                            #Sjekker om bestanden øker
        bøker()                                 #Kaller på funksjonen bøker()
    elif x == '2':                          #Sjekker om bestanden minker
        bminker()                               #Kaller på funksjonen bminker()
    else:
        print(x, 'er ikke et svar alternativ')  #Gir brukeren en feilmelding dersom de velger noe annet en om bestanden øker eller minker
    
    nyTest = input('ønsker du å gjøre testen på nytt? (ja eller j for en ny test): ')