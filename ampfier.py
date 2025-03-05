import random
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Conjuntos de aminoácidos
hidrofobicos = 'AILMFVWY'
cationicos = 'KRH'
todos_aas = 'ACDEFGHIKLMNPQRSTVWY'

# Dataset com exemplos positivos e negativos
data = {
    'sequence': [
        # Positivos (atividade antimicrobiana)
        'AILMFKRKRKRKRKRKRKRR',
        'WVYLMRHRHRHRHRHRHRHH',
        'FAVILKKRRKKRRKKRRKRR',
        'MILFAKRKRKRKRKRKRKRR',
        # Negativos (sem atividade antimicrobiana)
        'ACDEFGHNPQSTVWYACDEF',
        'NPQRSTVWYACDEFGHIKLM',
        'GHIKLMNPQRSTVWYACDEF',
        'TVWYACDEFGHIKLMNPQRS'
    ],
    'activity': [1, 1, 1, 1, 0, 0, 0, 0]  # 1 indica atividade antimicrobiana, 0 indica não atividade
}
df = pd.DataFrame(data)

# Vetorização de sequências
vectorizer = CountVectorizer(analyzer='char', ngram_range=(1, 2))
X = vectorizer.fit_transform(df['sequence'])
y = df['activity']

# Treinar o modelo
clf = RandomForestClassifier()
clf.fit(X, y)

# Avaliar o modelo (opcional)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(f'Acurácia do modelo em teste: {accuracy_score(y_test, y_pred):.2f}')

# Função para gerar candidatos com restrições desejadas
def gerar_peptideo():
    # Região N-terminal hidrofóbica (5 resíduos)
    n_terminal = ''.join(random.choices(hidrofobicos, k=5))
    # Região restante predominantemente catiônica (15 resíduos)
    restante = ''.join(random.choices(cationicos + 'AGPS', k=15))
    return n_terminal + restante

# Gerar novos candidatos
candidatos = [gerar_peptideo() for _ in range(100)]
X_candidatos = vectorizer.transform(candidatos)

# Realizar predições sobre os novos candidatos
predicoes = clf.predict_proba(X_candidatos)[:, 1]

# Filtrar candidatos com alta probabilidade de atividade (>0.8)
peptideos_promissores = [(pep, score) for pep, score in zip(candidatos, predicoes) if score > 0.8]

# Exibir resultados
print('\nPeptídeos promissores encontrados:')
for pep, score in peptideos_promissores:
    print(f'{pep} -> Probabilidade de atividade: {score:.2f}')
