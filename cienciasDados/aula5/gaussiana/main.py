import matplotlib.pyplot as plt
import numpy as np

# Dados coletados na nossa pesquisa real
tempos_sono = [6.5, 7, 5, 8, 7.5, 5.5, 6, 9, 7, 6.5, 4, 8.5, 7, 6]

# Cálculos estatísticos automáticos da nossa amostra
media = np.mean(tempos_sono)
desvio = np.std(tempos_sono, ddof=1)


distribuicao = np.random.normal(media, desvio, 500000)

print(len(distribuicao)) 


plt.hist(distribuicao, bins=15, edgecolor='black', color='skyblue')
plt.title('Simulação de Distribuição do Tempo de Sono')
plt.xlabel('Horas de Sono')
plt.ylabel('Frequência (Pessoas)')
plt.show()
