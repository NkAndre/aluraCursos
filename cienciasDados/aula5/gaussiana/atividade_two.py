import matplotlib.pyplot as plt
import numpy as np

# Parâmetros fornecidos pela pesquisa
media_pesquisa = 7
desvio_pesquisa = 1
populacao_simulada = 50000

# 1. Utilizando a distribuição Gaussiana (Normal) para gerar a amostra
dados_simulados = np.random.normal(media_pesquisa, desvio_pesquisa, populacao_simulada)

plt.figure(figsize=(10, 6))
plt.hist(dados_simulados, bins=30, edgecolor='black', color='lightgreen')

plt.title('Distribuição Simulada do Tempo de Sono (50.000 pessoas)', fontsize=14)
plt.xlabel('Horas de Sono', fontsize=12)
plt.ylabel('Frequência (Número de Pessoas)', fontsize=12)
plt.grid(axis='y', alpha=0.3)

plt.show()
