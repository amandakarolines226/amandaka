"""Dashboard de vendas com pandas."""
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv(r"C:\Users\Amanda\Downloads\vendas.csv", encoding="latin1", sep=';')

# remove espaços nos nomes das colunas
df.columns = df.columns.str.strip()
print(df.columns.tolist())
print("Colunas encontradas:", df.columns.tolist())

# converte a coluna 'Data' para formato de data
df["DATA"] = pd.to_datetime(df["DATA"])

print(df.columns)

# Verificar nomes reais das colunas
print("Colunas encontradas:", df.columns.tolist())

# Calcular total por linhas
df["Total"] = df["Quantidade"] * df ["Preco"]

# Mostrar resumo estatístico
print("RESUMO ESTATÍSTICO:")
print (df.describe())
print("\n TOTAL DE VENDAS DO PRODUTO")
print(df.groupby("Produto")["Total"].sum())

# Gráficos
vendas_produto = df.groupby("Produto")["Total"].sum()
vendas_dia = df.groupby("DATA")["Total"].sum()

plt.figure(figsize=(10, 5))

# Gráfico de barras
plt.subplot(1, 2, 1)
vendas_produto.plot(kind="bar", color= "skyblue")
plt.title("Vendas por produto")
plt.xlabel("Produto")
plt.ylabel("R$")

# Gráfico de linha
plt.subplot(1, 2, 1)
vendas_dia.plot(kind="line", marker= "o", color= "green")
plt.title("Vendas por dia")
plt.xlabel("DATA")
plt.ylabel("R$")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("relatorio_vendas.png")
plt.show()
