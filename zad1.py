import math


def ilosc_potrzebnych_paneli(dlugoscPodlogi, szerokoscPodlogi,dlugoscPaneli,szerokoscPaneli, iloscPaneliWOpakowaniu):


    iloscPaneliNaSzerokosc=szerokoscPodlogi/szerokoscPaneli
    iloscPaneliNaDlugosc=dlugoscPodlogi/dlugoscPaneli

    potrzebnaIlosc=iloscPaneliNaSzerokosc*iloscPaneliNaDlugosc
    potrzebaIprocenty=potrzebnaIlosc+(1/10)*potrzebnaIlosc
    potrzebneOpakowania=math.ceil(potrzebaIprocenty/iloscPaneliWOpakowaniu) #tylko zaokrglic do calosci
    return potrzebneOpakowania


print("Potrzeba : "+str(ilosc_potrzebnych_paneli(4, 4, 0.20, 1, 10)))





