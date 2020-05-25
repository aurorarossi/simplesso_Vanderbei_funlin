#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import division
from fractions import Fraction
from numpy import *
import funzioni_lineari as f
from IPython.display import display, Markdown

class Tableau:
    #inizializzazione
    def __init__(self, obj, prob_type):
        self.rows = []
        self.cons = []
        self.nonbasis = []
        self.basis=[]
        self.obj=[]
        if prob_type == 'max':
            self.obj =[f.l(x) for x in obj]
        elif prob_type == 'min':
            array=[f.l(x) for x in obj]
            for j in range(len(obj)):
                array[j].cambiosegni()
            for j in range(len(obj)):
                self.obj.append(array[j])
            
 
     #vincoli
    def aggiungi_vincolo(self, expression, value):
        self.cons.append(f.l(value))
        array=[f.l(x) for x in expression]
        for j in range(len(expression)):
            array[j].cambiosegni()
        self.rows.append(array)
        
        

    #print del tablau
    def mostra_tableau(self):
        s = ' '
        #prima riga di etichette
        s += '\t-'
        for i in range(len(self.obj)-1):
            s += '\t'+str(self.nonbasis[i])
        #colonna di etichette
        s += '\nz'
        for i in range(0,len(self.obj)):
            s += '\t' + (self.obj[i]).stringa()
        
        for i in range(len(self.rows)):
            s += '\n'+str(self.basis[i])
            for j in range(0,len(self.rows[i])):
                s += '\t' +(self.rows[i][j]).stringa()
        print(s)

    #print del tablau in markdown
    def mostra_tableau_markdown(self):
        s = '|\t| '
        #prima riga di etichette
        s += '-|'
        for i in range(len(self.obj)-1):
            s += str(self.nonbasis[i])+'|'
        s+='\n|'
        for i in range(len(self.obj)+1):
            s +='--' +'|'
        #colonna di etichette
        s += '\n|z|'
        for i in range(0,len(self.obj)):
            s +=  (self.obj[i]).stringa()+'|'
        
        for i in range(len(self.rows)):
            s += '\n|'+str(self.basis[i])+'|'
            for j in range(0,len(self.rows[i])):
                s +=  (self.rows[i][j]).stringa()+'|'
        display(Markdown(s))
        

    

    def crea_primo_tableau(self):
        for i in range(len(self.cons)):
            self.rows[i].insert(0,self.cons[i])
        self.obj = array([f.l([0])]+self.obj)
        
        dim = len(self.rows)
        dim2=len(self.obj)
        for i in range(dim):
            self.basis += ["s"+str(1+i)]
            
        for i in range(1,dim2):
            self.nonbasis += ["x"+str(i)]

    def pivot(self,row,col):
        r=0
        c=0
        #individuo riga e colonna associato a etichette
        while self.basis[r]!=str(row):
            r+=1
        while self.nonbasis[c]!=str(col):
            c+=1
        c=c+1
        e = self.rows[r][c]
        self.basis[r]=str(col)
        self.nonbasis[c-1]=str(row)
        assert e != 0
        #cambio coefficienti tabella tranne riga e colonna pivot
        for i in range(len(self.rows)):
            for j in range(len(self.obj)):
                if i!=r and j!=c:
                    ogg=self.rows[r][j].prod(self.rows[i][c])
                    ogg=ogg.prodinv(e)
                    ogg=ogg.cambiosegno1()
                    self.rows[i][j]=self.rows[i][j].plus(ogg)

        for j in range(len(self.obj)):
                if j!=c:
                    ogg=self.rows[r][j].prod(self.obj[c])
                    ogg=ogg.prodinv(e)
                    ogg=ogg.cambiosegno1()
                    self.obj[j]=self.obj[j].plus(ogg)

        self.obj[c]=self.obj[c].prodinv(e)
        
        for i in range(len(self.rows)):
            if i!=r:
                self.rows[i][c]=self.rows[i][c].prodinv(e)
                
        #cambio riga pivot
        for i in range(len(self.obj)):
            if i!=c:
                self.rows[r][i]=self.rows[r][i].cambiosegno1()
                self.rows[r][i]=self.rows[r][i].prodinv(e)
        self.rows[r][c].inv()

 
