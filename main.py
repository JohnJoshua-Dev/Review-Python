# Importando as bibliotecas
import os
import pandas as pd
import plotly.express as px

# percorrer todas as bases de dados venda (listar arquivos)
lista_arquivo = os.listdir("D:\Development\Pessoal\Python Review\Vendas")

tabela_total = pd.DataFrame() # esta é uma tabelavazia que estou criando para que sempre que ler os arquivos e adicione a tabela nesta que sera o agrupamento de todas as tabelas

for arquivo in lista_arquivo:
    # Tratar => tenho nessas bases de dados as bases de devolução mas eu so quero as de vendas então preciso filtrar
    # se tem "vendas" no nome do arquivo então
    if "vendas" in arquivo.lower():

    #importar base de dados
        tabela = pd.read_csv(f"D:\Development\Pessoal\Python Review\Vendas/{arquivo}")
tabela_total = tabela_total._append(tabela)  
print(tabela_total)

# Calcular produto mais vendido em quantidade
tabela_produto = tabela_total.groupby('Produto').sum()
tabela_produto = tabela_produto[["Quantidade Vendida"]].sort_values(by="Quantidade Vendida", ascending=False) # Celecionando colunas para aparecerem... e ordenando de forma decrescente com o sort
print(tabela_produto)

# Calculo do produto que mais faturou
tabela_total["Faturamento"] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby("Produto").sum()
tabela_faturamento = tabela_faturamento[["Faturamento"]].sort_values(by="Faturamento")
print(tabela_faturamento)

# Calculo de loja que mais faturou
tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']]
print(tabela_lojas)

#Grafico faturamento
grafico = px.bar(tabela_faturamento, x=tabela_faturamento.index, y='Faturamento', title='Faturamento por Produto', color=tabela_faturamento.index)
grafico.show()