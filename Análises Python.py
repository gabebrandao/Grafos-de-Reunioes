import pandas
'''import networkx as nx'''

#importando a base de dados 
dados= pandas.read_excel('Mapeamento de Reuniões.xlsx', 'Base de Dados Reuniões')

#Separando os dataframes por Cargo
dadosHead = dados.loc[dados['Cargo']=='Head']
dadosPm = dados.loc[dados['Cargo']=='PM']


'''posso criar um dicionário onde cada índice é o nome
da reunião e dentro dele temos uma lista com todos os 
participantes da reunião, assim posso criar o grafo com a
biblioteca.'''

