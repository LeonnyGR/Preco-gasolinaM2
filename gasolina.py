import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('./gasolina.csv')
data.head()
grafico = sns.barplot(data=data, x="dia", y="venda", ci=None, palette="pastel")
grafico.set(title='Preço da gasolina por dia', xlabel='Dia', ylabel='Preço(R$)');
plt.savefig('gasolina.png')