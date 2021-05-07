# -*- coding: utf-8 -*-
from collections import Counter
import json


nomes_temp=[]
linha = [0]
arquivo = open ("Entregas.txt","r")
arquivo_saida = open ("ranking.txt", "w")

data1 = "01/09/2020"

    
while linha != []:
    
    linha = arquivo.readline()
    linha_separada=linha.split('\t')
    data = linha_separada[1].split()[0]
    nome = linha_separada[2].rstrip()
    
    if data1 == data:
        
        nomes_temp.append(nome)
        
    else:
        arquivo_saida.write ( "\n \n" + data1 + "\n")
        for item in nomes_temp:
            dict_nomes = Counter ( nomes_temp )
            for key in dict_nomes:
            arquivo_saida.write ( json.dumps( Counter ( nomes_temp ) ) )
        data1 = data
        nomes_temp = []
        
    
        
    
    