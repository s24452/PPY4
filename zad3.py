#na male lub duze literki zamieniamy

def szyfrCezara(wiadomosc,klucz,alfabet=''):
    maleLitery = wiadomosc.lower()      #97-122
    litery = list(maleLitery)
    szyfr=[]
    wartosc = 0
    for i in range (0, len(litery)):

       a=litery[i]
       if(a.isalpha()):
        wartosc = ord(litery[i])+klucz
        if(wartosc>ord('z')):
            oIleWiekszaOdZ=wartosc-ord('z')
            nowaWartosc=ord('a')+oIleWiekszaOdZ-1
            szyfr.append(chr(nowaWartosc))
        else:
            szyfr.append((chr(wartosc)))
       else:
           szyfr.append(litery[i])




    zaszyfrowanaWiadomosc =''.join(szyfr)
    return zaszyfrowanaWiadomosc

print("Zaszyfrowana wiadomosc = "+str(szyfrCezara("Ana%n2asx" ,2)))
print(szyfrCezara("The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carrollna:",5))





