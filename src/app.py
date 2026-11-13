import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="AI Customer Analytics", layout="wide")


@st.cache_data
def carregar_dados():
    return pd.read_csv("data/clientes.csv", parse_dates=["data_contato"])


df = carregar_dados()

st.title("AI Customer Analytics")
st.caption("Dados sintéticos de atendimento ao cliente")

col1, col2, col3 = st.columns(3)
col1.metric("Total de contatos", len(df))
col2.metric("Tempo médio de resolução (min)", round(df["tempo_resolucao_min"].mean(), 1))
col3.metric("Nota média de satisfação", round(df["nota_satisfacao"].mean(), 2))

st.subheader("Visão geral")
graf1, graf2 = st.columns(2)

contatos_por_canal = df.groupby("canal").size().reset_index(name="contatos")
fig_canal = px.bar(contatos_por_canal, x="canal", y="contatos", title="Contatos por canal")
graf1.plotly_chart(fig_canal)

nota_por_categoria = (
    df.groupby("categoria")["nota_satisfacao"].mean().round(2).reset_index()
)
fig_nota = px.bar(
    nota_por_categoria,
    x="categoria",
    y="nota_satisfacao",
    title="Nota média de satisfação por categoria",
)
graf2.plotly_chart(fig_nota)

df["mes"] = df["data_contato"].dt.to_period("M").astype(str)
contatos_por_mes = df.groupby("mes").size().reset_index(name="contatos")
fig_mes = px.line(
    contatos_por_mes, x="mes", y="contatos", markers=True, title="Contatos por mês"
)
st.plotly_chart(fig_mes)

st.subheader("Amostra dos dados")
st.dataframe(df.head(20))