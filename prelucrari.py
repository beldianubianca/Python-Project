'''
Created on Jan 8, 2019

@author: Bianca
'''
from entitate import Entitate

#d:parcurge sirul s si il prelucreaza
#i:s
#o:
def li_r(s):
    c=0
    for string1 in s:
        intrebari=[]
        listaIntrebari=[]
        listaRaspunsuri=[]   
        for string in string1:
            listaIntrebari=[]
            listaRaspunsuri=[]
            elems =string.split("?")
            q = elems[0]
            a = elems[1]
            ra=a.split("\n")
            x=ra[0].split()
            listaIntrebari.append(q+"?")
            listaRaspunsuri.append(x)
            for i in range(0,len(listaIntrebari)):
                intrebari.append(Entitate(listaIntrebari[i],listaRaspunsuri[i]))
        for intrebare in intrebari:
            raspcorect=intrebare.getRaspuns()
            raspuns = (str(input(intrebare.getIntrebare()))).split()
    
            while(not verificareraspuns(raspuns, raspcorect) and c<=3):
                raspuns = (str(input(intrebare.getIntrebare()))).split()
                c=c+1
            if c==4:
                print(raspcorect)
                c=0
                break
            
#d: verifica daca raspunsul este corect
#i:raspunsul utilizatorului si raspunsul corect
#o: true daca raspunsul este corect si false in caz contrar       
def verificareraspuns(raspuns, raspcorect):
    cnt = 0
    for cuvant in raspuns:
        if cuvant.isdigit():
            nrcorect = None
            for str in raspcorect:
                if str.isdigit():
                    nrcorect = int(str)
            if(nrcorect == None):
                print("Raspuns gresit")
                return False
            if (nrcorect < int(cuvant)):
                print("Valoarea corecta este mai mica")
                return False
            elif (nrcorect > int(cuvant)):
                print("Valoarea corecta este mai mare")
                return False
            else:
                cnt += 1
        else:
            contine = cuvant in raspcorect
            if contine:
                cnt += 1
    if(cnt == 0):
        print("Respunsul nu este corect")
        return False
    if cnt < len(raspcorect):
        print("Respunsul este partial corect")
        return False
    print("Raspunsul este corect")
    return True