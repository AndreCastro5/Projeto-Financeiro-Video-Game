#libs necessarias 

#libs para modelagem de matrizes 
import numpy as np 
import pandas as pd 

#libs para análises gráficas 
import matplotlib.pyplot as plt
import seaborn as sns 

#lib para ignorar avisos 
import warnings 

#desabilitando avisos 
warnings.filterwarnings('ignore')

#lib importação de arquivo 
import os 

os.chdir('C:\\Users\\andre\\OneDrive\\Área de Trabalho\\python\\Projeto vendas de videogames')

#lendo os dados 
Base_Dados = pd.read_csv('PS4_GamesSales.csv', encoding='latin-')

# Verificando 
Base_Dados.head()

#Dimensão 
Base_Dados.shape 

#nulos
Base_Dados.isnull().sum()

# Nulos Graficos 
plt.figure(figsize=(14,5))
plt.title('Verificando campos nulos')
sns.heatmap(Base_Dados.isnull(), cbar=False);
#plt.show()

#Retirando Valores nulos 
Base_Dados.dropna (inplace = True)

#Estatisticas 
Base_Dados.describe()

#Tamanho da imagem 
plt.figure(figsize=(10,5))

#Titulo 
plt.title('Quantidade de Vendas Globais (mi)', loc='left',fontsize=14)

#Grafico 
sns.barplot( data=Base_Dados, x='Year', y='Global', ci=None, color='#69b3a2', estimator=sum) 

#Label 
plt.ylabel('Quantidade de vendas (mi)');
#plt.show()

# Retirar os anos 
Base_Dados = Base_Dados.loc[(Base_Dados['Year'] !=2019) & (Base_Dados['Year'] != 2020)]

#Verificar
Base_Dados.head()

#Tamanho 
plt.figure(figsize=(12,5))

#Estilo 
plt.style.use('ggplot')

#titulo 
plt.title('Distribuição das Vendas Globais', loc='left', fontsize=14)

#plot
sns.kdeplot(Base_Dados['Global'], shade= True, bw=1, color='#96a8a8', linewidth=2.5);
#plt.show()

Base_Dados.groupby(by=['Year']).sum()

# Tamanho 
plt.figure(figsize = (10, 4))

#Titulo
plt.title('Análise da distribuição Global (mi)')

#Plot
sns.boxplot( data = Base_Dados, x='Year', y='Global');

#plt.show()

Base_Dados.loc[Base_Dados['Global']>=10]

Base_Dados

Analise = Base_Dados.groupby(by=['Year']).sum().reset_index()

#analisando a proporção dos 100% de cada continente comparado ao total 
America = [America/Total * 100 for America, Total in zip(Analise['North America'], Analise ['Global'])]
Europa = [Europa/Total * 100 for Europa, Total in zip(Analise['Europe'], Analise ['Global'])]
Japao = [ Japao / Total * 100 for Japao, Total in zip( Analise['Japan'], Analise['Global'] ) ]
Mundo = [ Mundo / Total * 100 for Mundo, Total in zip( Analise['Rest of World'], Analise['Global'] ) ]

print(America, Europa, Japao, Mundo)

#Tamanho 
plt.figure(figsize=(10,5))

# Largura barra no gráfico 
Largura_Barra = 0.85
Rotulos = Analise ['Year']
Grupos = [0,1,2,3,4,5]

#titulo 
plt.title('Análise distribuição por continentes')

# plot da america 
plt.bar( Grupos, America, width= Largura_Barra, color='#b5ffb9', edgecolor='white')

# Plot da Europa
plt.bar( Grupos, Europa, bottom=America, width=Largura_Barra, color='#f9bc86', edgecolor='white' )

#plot do Japão 
plt.bar(Grupos, Japao, bottom=[A + B for A, B in zip(America, Europa)], width= Largura_Barra, color='#a3acff', edgecolor='White')

# Labels
plt.xticks(Grupos, Rotulos)
plt.xlabel('Grupo')
plt.ylabel('Distribuição %')

#Legenda
plt.legend(['America N', 'Europa', 'Japão','Mundo'], loc='upper left', bbox_to_anchor=(0.15, -0.1), ncol=4);

#plt.show()

Base_Dados['Publisher'].unique()

from sklearn.preprocessing import LabelEncoder
funcao_Label = LabelEncoder()

Base_Dados['Produtor']= funcao_Label.fit_transform(Base_Dados['Publisher'])
Base_Dados['Genero'] = funcao_Label.fit_transform(Base_Dados['Genre'])
Base_Dados['Jogo']= funcao_Label.fit_transform(Base_Dados['Game'])

Base_Dados.head()

Paleta_Cores = sns.color_palette('husl', 8)
print(Paleta_Cores);

plt.figure(figsize=(20,5))
plt.title('Análise dos produtores de Game (mi)')
sns.scatterplot(data=Base_Dados, x='Produtor', y='Global', color= Paleta_Cores[0]);
plt.show()

plt.figure(figsize=(20,5))
plt.title('Análise dos generos dos Games (mi)')
sns.scatterplot(data=Base_Dados, x='Genero', y='Global', color= Paleta_Cores[0]);
plt.show()

plt.figure(figsize=(20,5))
plt.title('Análise dos Games(mi)')
sns.scatterplot(data=Base_Dados, x='Jogo', y='Global', color= Paleta_Cores[0]);
plt.show()

# Relatorio 

#Tamanho da imagem 
fig, ax = plt.subplots(figsize=(18,15))

#Cor de fundo 
Cor_Fundo = '#f5f5f5'
ax.set_facecolor(Cor_Fundo)
fig.set_facecolor(Cor_Fundo)

# Estilo dos gráficos 
plt.style.use('seaborn')

#Titulo da figura 
plt.suptitle('Python para Análise de Dados \n   Análise Mercado de Games PS4', fontsize=15, color='#404040', fontweight=600)

#Parametros para o grid
Linhas = 3 
Colunas = 2 

#Acessando gráfico 1 
plt.subplot(Linhas, Colunas, 1)

#Titulo
plt.title("Quantidade de Vendas Globais (mi)", loc='left', fontsize=14)

#Grafico
plt.bar(Base_Dados['Year'], Base_Dados['Global'], color='#69b3a2')

#Label
plt.ylabel('Quantidade Vendas (mi)')

#Acessando gráfico 2 
plt.subplot(Linhas, Colunas, 2)

#titulo 
plt.title('Análise de distribuição Global (mi)')

#Plot
sns.boxplot(data= Base_Dados, x='Year', y='Global')

#Acessando gráfico 3
plt.subplot(Linhas, Colunas, 3)
#Largura da barra no gráfico 
Largura_Barra = 0.85
Rotulos = Analise['Year']
Grupos = [0,1,2,3,4,5]
#titulo 
plt.title('Análise distribuição por continentes', loc='left', fontsize=14)
#plot da America 
plt.bar(Grupos, America, width=Largura_Barra, color= '#b5ffb9', edgecolor='white')
#plot da Europa
plt.bar(Grupos, Europa, bottom=America, width= Largura_Barra, color='#f9bc86', edgecolor='white')
#plot do Japão 
plt.bar(Grupos, Japao, bottom=[A + B for A, B in zip(America, Europa)], width=Largura_Barra, color= '#a3acff', edgecolor='white')
#plot do resto do mundo 
plt.bar(Grupos, Mundo, bottom=[A + B + C for A, B, C in zip(America, Europa, Japao)], width= Largura_Barra, color='#d3acfe', edgecolor='white')
#Labels 
plt.xticks(Grupos, Rotulos)
plt.ylabel('Distribuição %')
# Legenda 
plt.legend(['America N', 'Eupora', 'Japão', 'Mundo'], loc= 'upper left', bbox_to_anchor=(-0.01, -0.1), ncol=4); 

#Acessando gráfico 4
plt.subplot(Linhas, Colunas, 4)
plt.title('Análise dos produtores de Game (mi)', loc='left', fontsize=14)
sns.scatterplot(data= Base_Dados, x='Produtor', y='Global', color= Paleta_Cores[0]);

#Acessando gráfico 5 
plt.subplot(Linhas, Colunas, 5)
plt.title('Análise dos generos do Game (mi)', loc= 'left', fontsize=14)
sns.scatterplot(data= Base_Dados, x='Genero', y='Global', color = Paleta_Cores[0]);

#Acessando gráfico 6
plt.subplot(Linhas, Colunas, 6)
plt.title('Análise dos Games (mi)', loc='left', fontsize=14)
sns.scatterplot(data=Base_Dados, x='Jogo', y='Global', color=Paleta_Cores[0]);

#Ajustar o layout
plt.subplots_adjust(hspace=0.90, wspace=0.40) 
plt.show()