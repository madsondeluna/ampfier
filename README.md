# Design de Peptídeos Antimicrobianos utilizando Machine Learning

Este projeto implementa um pipeline básico utilizando aprendizado de máquina (Random Forest Classifier) para o design e predição de atividade antimicrobiana em peptídeos curtos (20 aminoácidos), catiônicos e com uma região N-terminal hidrofóbica definida.

## Descrição do Projeto

O script em Python gera candidatos de peptídeos com características específicas:
- **20 resíduos totais**.
- **5 resíduos iniciais hidrofóbicos**.
- **15 resíduos predominantemente catiônicos ou neutros**.

Após gerar os candidatos, utiliza um modelo de aprendizado de máquina treinado com sequências positivas e negativas para prever a probabilidade dos novos candidatos possuírem atividade antimicrobiana.

## Pré-requisitos

- Python 3.x
- pandas
- scikit-learn

Instale as dependências com:
```bash
pip install pandas scikit-learn
```

## Estrutura do Código

- **Dataset**: O script inclui um pequeno conjunto de dados (fictício para demonstração) contendo sequências com e sem atividade antimicrobiana.

- **Pré-processamento**: Utiliza `CountVectorizer` com análise por caracteres e n-gramas (1-2) para transformar as sequências de aminoácidos em características numéricas compreensíveis para o modelo.

- **Modelo de ML**: Um classificador `RandomForestClassifier` é treinado utilizando os dados preparados.

- **Geração de Candidatos**: Função específica cria sequências respeitando as restrições bioquímicas especificadas:
  - Região N-terminal hidrofóbica.
  - Região restante catiônica/neutra.

- **Predição**: O modelo treinado é utilizado para prever novos peptídeos gerados, indicando aqueles com maior potencial antimicrobiano (probabilidade > 0.8).

## Como executar

Clone o repositório e execute:

```bash
python seu_script.py
```

A saída mostrará a acurácia do modelo e os peptídeos promissores identificados pelo algoritmo.

## Exemplo de Saída

```
Acurácia do modelo em teste: 1.00

Peptídeos promissores encontrados:
WYFILRRRKRHKHHRKHGHP -> Probabilidade de atividade: 0.90
VYYFVRHKRRHRKHHRKRRA -> Probabilidade de atividade: 0.85
...
```

## Notas
- Este exemplo utiliza um dataset fictício. Para resultados reais, utilize um conjunto validado e robusto de sequências.
- O modelo pode ser melhorado com técnicas mais avançadas (e.g., redes neurais, deep learning) para resultados mais precisos.

## Autor

Madson Aragão

## Licença

Este projeto está licenciado sob a licença MIT.
