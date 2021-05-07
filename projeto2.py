# -*- coding: utf-8 -*-
from collections import Counter

from operator import itemgetter
entregadores = []
nomes_temp=[]
linha = [0]
arquivo = open ("c:/Users/eduar/OneDrive/Área de Trabalho/Entregas.txt","r")
arquivo_saida = open ("c:/Users/eduar/OneDrive/Área de Trabalho/ranking.txt", "w")

data1 = "01/09/2020"

    
while linha != []:
    
    linha = arquivo.readline()
    linha_separada=linha.split('\t')
    data = linha_separada[0].split()[0]
    nome = linha_separada[1].rstrip()
    
    if data1 == data:
        
        nomes_temp.append(nome)
        
    else:
        entregadores = []
        entregador = []
        arquivo_saida.write ( "\n\n" + data1 + "\n")
        dict_nomes = Counter ( nomes_temp )
        data1 = data
        nomes_temp = []

        for key in dict_nomes:
            entregador = [ key , dict_nomes[key] ]
            entregadores.append(entregador)
        for item in entregadores:
            entregadores=sorted(entregadores, key=itemgetter(1),reverse=True)
        
        for item in entregadores:
            arquivo_saida.write(item[0] + "\t" +str(item[1]) + "\n")
        
        
        
        
    
        
    
    