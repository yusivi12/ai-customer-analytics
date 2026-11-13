import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 1000

canais = ["App", "Site", "Telefone", "Chat"]
categorias = ["Atendimento", "Cobrança", "Produto", "Entrega", "Cadastro"]

df = pd.DataFrame({
    "id_cliente": range(1, n + 1),
    "data_contato": pd.date_range("2026-01-01", periods=n, freq="8h"),
    "canal": rng.choice(canais, n),
    "categoria": rng.choice(categorias, n),
    "tempo_resolucao_min": rng.integers(2, 120, n),
    "nota_satisfacao": rng.integers(1, 6, n),
})

df.to_csv("data/clientes.csv", index=False)
print("Arquivo data/clientes.csv criado com", len(df), "linhas")