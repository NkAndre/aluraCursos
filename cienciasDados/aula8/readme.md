# 📊 Simulação Estatística e Validação de Modelos com Python

Este projeto foi desenvolvido como parte de um estudo prático sobre **Estatística Computacional** e **Introdução à Validação de Modelos (Machine Learning)**. O objetivo principal é compreender como simular o comportamento de dados do mundo real utilizando distribuições matemáticas e validar hipóteses por meio de programação.

---

## 🚀 O que o projeto faz?

O projeto está dividido em duas partes fundamentais:
1. **Simulação e Validação de Dados Reais:** A partir de uma pequena amostra real de horas de sono, calculamos a média e o desvio padrão para gerar uma simulação Gaussiana em larga escala (de 1.000 a 500.000 pessoas). Usamos técnicas de normalização e máscaras booleanas para validar matematicamente a precisão do modelo teórico em relação a novas amostras coletadas.
2. **Análise de Volatilidade vs. Estabilidade:** Um script comparativo que demonstra visualmente a diferença entre modelar fenômenos estáveis (como características biológicas) e fenômenos altamente voláteis e caóticos (como o mercado financeiro/câmbio).

---

## 🛠️ Tecnologias Utilizadas

*   **Python 3.8+**
*   **NumPy:** Para processamento numérico, geração de distribuições normais (`np.random.normal`) e cálculo de métricas estatísticas (`np.mean`, `np.std`).
*   **Matplotlib:** Para a construção de histogramas normalizados (`density=True`) e gráficos de linhas temporais comparativos.

---

## 📈 Conceitos Estatísticos Aplicados

*   **Distribuição Normal (Gaussiana):** Modelagem de dados em formato de sino, onde a maior concentração de pessoas está próxima aos valores centrais (média).
*   **Intervalos de Confiança (Regra Empírica):** Verificação de que ~68% dos dados se concentram dentro de 1 desvio padrão em relação à média.
*   **Normalização de Gráficos:** Uso do parâmetro `density=True` para transformar dados de contagem absoluta em probabilidade proporcional, permitindo a comparação visual justa entre amostras de tamanhos drasticamente diferentes.
*   **Dados de Treino vs. Validação:** Separação rígida de dados históricos para construir o modelo e dados inéditos para testar sua capacidade de generalização no mundo real.

---

## 💻 Como Rodar o Projeto

1. Certifique-se de ter o Python instalado na sua máquina.
2. Instale as dependências necessárias executando o comando abaixo no seu terminal:
   ```bash
   pip install matplotlib numpy
   ```
3. Execute qualquer um dos scripts principais desenvolvidos ao longo do módulo para visualizar os histogramas e as análises de dispersão.

---

## 📝 Estrutura das Análises Práticas

### Cenário de Estabilidade vs. Volatilidade
Ao final do projeto, simulamos o comportamento de dois extremos de previsibilidade ao longo de 30 dias:
*   **Fenômeno Estável (Altura Média):** Apresenta micro-oscilações irrelevantes ao redor de uma média fixa. É altamente previsível.
*   **Fenômeno Volátil (Preço de Câmbio):** Segue o conceito de *random walk* (passeio aleatório), onde choques diários de mercado acumulam incerteza a curto prazo, tornando a previsão extremamente complexa.

---

## 🧑 Autor

Desenvolvido por André durante a jornada de aprendizado na plataforma Alura.
