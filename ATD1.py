import pandas as pd

url="https://raw.githubusercontent.com/kunkaweb/nlp-class-resources/master/hospital-data/patients.csv"

#abrindo o arquivo csv e carregando-o em um dataFrame
df=pd.read_csv(url)

#quantidade de linhas e colunas
df.shape

#quantidade de pacientes por gênero e plotando um histograma
import matplotlib.pyplot as plt
# Atualiza tamanho padrão dos gráficos
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)})
contagemPacientes=df['gender'].value_counts()
print(contagemPacientes)
contagemPacientes.plot(kind='bar', title='Quantidade de Pacientes por Gênero', color=['pink','blue'])
plt.xlabel('Gênero')
plt.ylabel('Total de Pacientes')
plt.xticks(rotation=0) # Deixa o texto 'M' e 'F' na horizontal
plt.show()

#criando coluna para representar se o paciente é ou não nativo
df['Native']=df['ethnicity']=='american'

#mostrando pacientes de cada raça em um gráfico de barras
contagemRaca=df['race'].value_counts()
print(contagemRaca)
contagemRaca.plot(kind="bar", title="Quantidade de Pacientes por Raça")
plt.ylabel("Número de Pacientes")
plt.xticks(rotation=0)
plt.show()

#quantidade de valores numero de cada coluna
df.isnull().sum()

#etnia com maior uso de opióides
diagnosticoPositivo=df[df['prior_opioid_abuse_diag']==1]
contagemEtinias=diagnosticoPositivo['ethnicity'].value_counts()
print(contagemEtinias)
etniaCamp=contagemEtinias.idxmax()
print(f"A etnia com mior diagnosticos positivos para opióides é {etniaCamp}")

#indice de correlação entre as colunas
import seaborn as sns
# Importa biblioteca matplotlib
import matplotlib.pyplot as plt
# Atualiza tamanho padrão dos gráficos
plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)})
matriz_cor=df.corr(numeric_only=True)
sns.heatmap(matriz_cor,
    annot=True,
    fmt=".2f",
    cmap='coolwarm',
    linewidths=0.5
)
plt.title('Índice de Correlação')
plt.show()

#removendo colunas
df=df.drop(columns=['maiden','passport','drivers','prefix','suffix','ssn','first','last'])

#traduzindo o nome das colunas restantes para portugues
df=df.rename(columns={'pat_id':'id','birth_date':'Data_aniversario',
                      'death_date':'dia_morte','marital':'Estado civil',
                      'race':'raça','ethnicity':'etnia','gender':'genero',
                      'birthplace':'natalidade','address':'endereco',
                      'prior_opioid_abuse_diag':'diagnostico',
                      'native':'nativo'  
            })

#Extraindo arquivo .csv
# df.to_csv('pacientes_processados.csv', index=False)