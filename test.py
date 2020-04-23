'''
Created on Jan 8, 2019

@author: Bianca
'''
import prelucrari
from entitate import Entitate
def test_verificareraspuns():
    assert prelucrari.verificareraspuns("33","33")==True
    assert prelucrari.verificareraspuns("Stefan","8")==False
    assert prelucrari.verificareraspuns("55","99")==False
    assert prelucrari.verificareraspuns("Ana","Ana")==True
    assert prelucrari.verificareraspuns("A","b")==False
    print("ok")
test_verificareraspuns()

def testEntitate():
    e1=Entitate("intrebare",6)
    assert e1.getIntrebare()=="intrebare"
    assert e1.getRaspuns()==6
    e1.setRaspuns(7)
    e1.setIntrebare("int2")
    assert e1.getIntrebare()=="int2"
    assert e1.getRaspuns()==7
    print("ok")
testEntitate()
def test_eq():
    e1=Entitate("intrebare",7)
    e2=Entitate("intrebare",7)
    assert(e1==e2)
    e1.setRaspuns(8)
    e2.setRaspuns(9)
    assert(e1!=e2)
    print("ok")
test_eq()
def test_gt():
    e1=Entitate("int",9)
    e2=Entitate("int",7)
    assert(e1>e2)
    print("ok")
test_gt()
def test_lt():
    e1=Entitate("int",9)
    e2=Entitate("int",7)
    assert(e1>e2)
    print("ok")
test_lt()
