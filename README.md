# Grafos-de-Reunioes
#Este código tem o objetivo de criar um grafo a partir de uma tabela de reuniões, onde a primeira coluna é o tipo da reunião e a segunda são os participantes da reunião.

import pandas #Biblioteca de dados 
import networkx as nx  #Biblioteca de Grafos
import itertools  #Biblioteca de análise combinatória

##dados= pandas.read_excel('simulação.xlsx')
dados= pandas.read_excel('simulação 2.xlsx')
'''
Criar um dicionário onde o índice é a reunião e dentro, uma lista com todos
os participantes da reunião
obs: Talvez apenas o primeiro índice dalista possa ser a reunião (Elaborar)
'''

#Função que transforma o dataframe em dicionário

def dicionario(df):
    dic=dict()
    for i in range(len(dados)):
        #Preciso separar os participantes por ';' usando o split
        dic[dados['Reunião'][i]]=list(dados['Participantes'][i].split(';'))
    return dic

dic=dicionario(dados)

''' 
Agora temos um dicionário onde os índices (keys) são as reuniões e os 
valores (values) são os participantes das reuniões, vale lembrar que os participantes
estão em qualquer ordem.
'''    

#Função para tirar todas as conexões (Cria uma lista de tuplas com as conexões)
#para depois adicinar todos os vértices
grafo= nx.Graph()

def conexo(dic):
    for key in dic.keys():
        lista=dic[key]
        grafo.add_edges_from(list(itertools.combinations(lista, 2)))
    return grafo

conexo(dic)

nx.draw_networkx(grafo, with_labels=True)


'''
O que preciso fazer: Diferenciar as combinações 2 a 2, para isso retirar 
redundâncias como por exemplo (1,2) e (2,1); colocar rótulos nos vértices
para representarem cada um uma reunião.

Adicionar Pesos nos nós dos grafos

Distância pode representar densidade de reuniões, mapa de quem se comunica com quem, 
pra ver se tem silos dentro da empresa.

'''
