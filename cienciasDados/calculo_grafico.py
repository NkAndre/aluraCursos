import matplotlib.pyplot as plt
import numpy as np

# dados e cálculos
atividade_fisica = [2, 3, 4, 5, 5, 6, 6, 7, 8, 20]
media = np.mean(atividade_fisica)
mediana = np.median(atividade_fisica)

# criação do histograma
plt.figure(figsize=(8, 5))
plt.hist(atividade_fisica, bins=5, edgecolor='black', alpha=0.7, color='skyblue')

# adicionando as linhas verticais com axvline
plt.axvline(media, color='red', linestyle='--', linewidth=2, label=f'Média ({media})')
plt.axvline(mediana, color='green', linestyle='-', linewidth=2, label=f'Mediana ({mediana})')

# rótulos e legendas
plt.xlabel('Horas Semanais de Atividade Física')
plt.ylabel('Frequência')
plt.title('Distribuição de Horas de Atividade Física')
plt.legend()


plt.grid(axis='y', linestyle='--', alpha=0.3)

plt.show()