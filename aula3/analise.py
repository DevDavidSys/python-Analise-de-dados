from os import error, path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn import metrics

tabela = pd.read_csv(r"C:\Users\DAVI\Documents\GitHub\Python-Analise-de-dados\aula3\advertising.csv")
print(tabela.info())
sns.heatmap(tabela.corr(),annot=True)
plt.show()

sns.pairplot(tabela)
plt.show()
y = tabela["Vendas"]
x = tabela.drop("Vendas", axis=1)

x_treino,x_teste,y_treino,y_teste = train_test_split(x,y,test_size=0.3,random_state=1)

modelo_regressao = LinearRegression()
modelo_arvore = RandomForestRegressor()

modelo_regressao.fit(x_treino,y_treino)
modelo_arvore.fit(x_treino,y_treino)

previsao_regressao = modelo_regressao.predict(x_teste)
previsao_arvore = modelo_arvore.predict(x_teste)

print(metrics.r2_score(y_teste,previsao_regressao))
print(metrics.r2_score(y_teste,previsao_arvore))

tabela_auxiliar = pd.DataFrame()
tabela_auxiliar["y_teste"] = y_teste
tabela_auxiliar["Previsao Arvore"] = previsao_arvore
tabela_auxiliar["Previsao Regressao"] = previsao_regressao

plt.figure(figsize=(15,5))
sns.lineplot(data=tabela_auxiliar)
plt.show()

sns.barplot(x=tabela_auxiliar.columns,y=modelo_arvore.feature_importances_)
plt.show()