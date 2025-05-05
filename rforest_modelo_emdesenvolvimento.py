import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

df = pd.read_csv('Dataset_Estoque_Completo.csv')

print(df)

df['Periodo_Compra'] = pd.to_datetime(df['Periodo_Compra'])
df['month'] = df['Periodo_Compra'].dt.month
df['year'] = df['Periodo_Compra'].dt.year

print(df)

le = LabelEncoder()
df['Tipo_Pneu_cod'] = le.fit_transform(df['Tipo_Pneu'])

print(df)

df.columns

x = df[['month', 'year','Tipo_Pneu_cod']]
y = df[['Volume_Compra']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,random_state=42)

param_grid = {'n_estimators':[100, 200],
'max_depth':[5, 10, None], 'min_samples_split':[2,5]}

model = RandomForestRegressor(random_state=42)

grid_search = GridSearchCV(estimator=model, param_grid=param_grid,cv=5,scoring='neg_mean_absolute_error',n_jobs=-1)
                           
grid_search.fit(x_train, y_train)


best_model = grid_search.best_estimator_

print("Melhores Hiperparametros:", grid_search.best_params_)

print("Melhor Modelo", best_model)

y_pred = best_model.predict(x_test)
mae = mean_absolute_error(y_test, y_pred)


print(f"Erro medio absoluto: {mae:.2f}")

# Recriar coluna de data a partir de ano e mês (se ainda não tiver feito)

resultados = x_test.copy()
resultados['year'] = resultados['year'].astype(str)
resultados['month'] = resultados['month'].astype(str).str.zfill(2)
resultados['Data'] = pd.to_datetime(resultados['year'] + '-' + resultados['month'] + '-01')

# Criar nova coluna só com o nome do mês (abreviado ou completo)
resultados['MesNome'] = resultados['Data'].dt.strftime('%b')  # Use '%B' para nome completo em português

# Ordenar pelo tempo, se necessário
resultados = resultados.sort_values('Data')

resultados['Volume_Real'] = y_test.values
resultados['Volume_Previsto'] = y_pred

resultados['tipo_pneu_string'] = Tipo_Pneu_cod


resultados.to_excel('resultadorforest.xlsx', index=False)

import matplotlib.pyplot as plt
import numpy as np

# 1. Criar coluna combinada com mês/ano e tipo de pneu
resultados['Grupo'] = resultados['Data'].dt.strftime('%b/%Y') + ' - ' + resultados['Tipo_Pneu_cod'].astype(str)

# 2. Selecionar as colunas para plotagem
categorias = resultados['Grupo']
valores_reais = resultados['Volume_Real']
valores_previstos = resultados['Volume_Previsto']

# 3. Gerar posições no eixo X
x = np.arange(len(categorias))  # posição de cada barra
largura = 0.4  # largura das colunas

# 4. Plotar gráfico de colunas lado a lado
plt.figure(figsize=(14, 6))
plt.bar(x - largura/2, valores_reais, width=largura, label='Real')
plt.bar(x + largura/2, valores_previstos, width=largura, label='Previsto')

plt.xticks(x, categorias, rotation=90)
plt.xlabel("Mês/Ano + Tipo de Pneu")
plt.ylabel("Volume de Compra")
plt.title("Comparação: Volume Real vs Previsto")
plt.legend()
plt.tight_layout()
plt.grid(axis='y')
plt.show()