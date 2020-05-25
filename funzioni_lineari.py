#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import division
from fractions import Fraction
from numpy import *

class l:
    
    def __init__(self,coef):
        self.coef=[]
        self.var=[]
        if type(coef)==int or type(coef)==float:
            self.coef.append(Fraction(coef))
        else:
            for i in range(len(coef)):
                if type(coef[i])==int or type(coef[i])==float:
                    self.coef.append(Fraction(coef[i]))
                if type(coef[i])==str:
                    self.var.append(coef[i])
        
    def stringa(self):
        s=str(self.coef[0])
        for i in range(len(self.var)):
            if self.coef[i+1]>0 and self.coef[i+1]!=1:
                s+='+'+str(self.coef[i+1])+self.var[i]
            if self.coef[i+1]==1:
                s+='+'+self.var[i]
            if self.coef[i+1]==-1:
                s+='-'+self.var[i]
            if self.coef[i+1]<0 and self.coef[i+1]!=-1:
                s+=str(self.coef[i+1])+self.var[i]
        return s

    def aggcoef(self,c):
        self.coef.append(c)

    def aggvar(self,v):
        self.var.append(v)
        
        
    def plus(self,v):
        somma=l([])
        totinds=[]
        totindv=[]
        indself=[]
        indv=[]
        somma.aggcoef(v.coef[0]+self.coef[0])
        for i in range(len(self.var)):
            for j in range(len(v.var)):
                if self.var[i]==v.var[j]:
                    somma.aggcoef(self.coef[i+1]+v.coef[j+1])
                    somma.aggvar(self.var[i])
                    indself.append(i)
                    indv.append(j)
        for i in range(len(self.var)):
            totinds.append(i)
        for j in range(len(v.var)):
            totindv.append(j)
        for i in range(len(indself)):
            totinds.remove(int(indself[i]))
        for j in range(len(indv)):
            totindv.remove(int(indv[j]))
        for i in range(len(totinds)):
            somma.aggcoef(self.coef[totinds[i]+1])
            somma.aggvar(self.var[totinds[i]])
        for j in range(len(totindv)):
            somma.aggcoef(v.coef[totindv[j]+1])
            somma.aggvar(v.var[totindv[j]])
        return somma

    def cambiosegni(self):
        for i in range(len(self.coef)):
            self.coef[i]=-self.coef[i]

    def cambiosegno1(self):
        n=l([])
        for i in range(len(self.coef)):
            n.aggcoef(-self.coef[i])
        for j in range(len(self.var)):
            n.aggvar(self.var[j])
        return n
        

    def prod(self,v):
        pr=l([])
        for i in range(len(self.coef)):
            pr.aggcoef(v.coef[0]*self.coef[i])
        for j in range(len(self.var)):
            pr.aggvar(self.var[j])
        return pr

    def prodinv(self,v):
        pr=l([])
        for i in range(len(self.coef)):
            pr.aggcoef((1/v.coef[0])*self.coef[i])
        for j in range(len(self.var)):
            pr.aggvar(self.var[j])
        return pr

    def inv(self):
        self.coef[0]=(1/self.coef[0])
            

            
            
            
        
            
        
        
        

    
