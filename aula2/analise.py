#passo 1:importar a base de dados
#passo 2: Visualizar a base de dados
#passo 3: Verificar a integridade das bases de dados
#passo 4:Tratamento da base de dados
#passo 5: Análise Inicial (Análise Exploratória)
#passo 6: Olhar a característica do seu cliente e ver como a caracteristica impacta no cancelamento

#kaggle - analise de dados
import plotly.express as px
import pandas as pd
#passo 1  
tabela = pd.read_csv("C:/Users/DAVI/Documents/GitHub/Python-Analise-de-dados/aula2/telecom_users.csv")
#passo 2
tabela["TotalGasto"]=pd.to_numeric(tabela["TotalGasto"],errors="coerce")#transforma a coluna total gasto para número
#passo 4
tabela = tabela.dropna(how="all",axis=1)
tabela = tabela.dropna(how="any",axis=0)
#retira os valores vazios da tabela

print(tabela.info())

#passo 5

for coluna in tabela:
    grafico = px.histogram(tabela,x=coluna,color="Churn")
    grafico.show()




