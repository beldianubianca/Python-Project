from entitate import Entitate
import prelucrari
#from random import shuffle
#file=open("q&a","r")

#d: citeste un fisier si adauga in s tot continutul sau
#i:fisierul file si lista s
#o:lista s
def citire(file,s ):
    file=open(file,"r")
    f=file.readlines()
    s.append(f)
    return s
    
s=[]
#file2=open("q&a","r")
s = citire("matematica", s)
#file3=open("q&a3","r")
s=citire("istorie",s)
#file4=open("q&a4","r")
s=citire("literatura",s)
s=citire("geografie",s)
#print(s)
#listaIntrebari=[]
#listaRaspunsuri=[]

def game():
    intrebari=[]
    #global intrebari
    print("Buna!","\n","Apasa 1 pentru a incepe.")
    start=int(input( ))
    c=0
    if(start==1):
        prelucrari.li_r(s)


game()
