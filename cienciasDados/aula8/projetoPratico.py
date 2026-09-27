import matplotlib.pyplot as plt
import numpy as np

# Configurando uma semente para gerar sempre os mesmos dados simulados
np.random.seed(42)

# Período de tempo da simulação (30 dias)
dias = np.arange(1, 31)

# 1. Simulação Estável: Altura Média de uma Turma (em cm)
# Pequenas oscilações irrelevantes ao redor de uma média de 165 cm
altura_media = 165 + np.random.normal(loc=0, scale=0.15, size=30)

# 2. Simulação Volátil: Preço de uma Moeda Estrangeira (em R$)
# Começa em R$ 5,00 e cada dia sofre uma variação percentual imprevisível
preco_moeda = [5.00]
for _ in range(29):
    # O próximo preço sofre um choque de até 3% para cima ou para baixo
    proximo_preco = preco_moeda[-1] * (1 + np.random.normal(loc=0, scale=0.03))
    preco_moeda.append(proximo_preco)
preco_moeda = np.array(preco_moeda)

# Criando a estrutura dos gráficos lado a lado
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Plotando o Gráfico Estável
ax1.plot(dias, altura_media, marker='o', color='green', linewidth=2)
ax1.set_title('Fenômeno Estável: Altura Média de Estudantes', fontsize=12)
ax1.set_xlabel('Dias')
ax1.set_ylabel('Altura (cm)')
ax1.set_ylim(160, 170) # Mantém escala visual justa
ax1.grid(True, alpha=0.3)

# Plotando o Gráfico Volátil
ax2.plot(dias, preco_moeda, marker='s', color='red', linewidth=2)
ax2.set_title('Fenômeno Volátil: Preço de Câmbio de Moeda', fontsize=12)
ax2.set_xlabel('Dias')
ax2.set_ylabel('Preço (R$)')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
