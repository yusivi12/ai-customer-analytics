\# AI Customer Analytics



Dashboard interativo de análise de atendimento ao cliente, feito em Python.



> \*\*Aviso:\*\* todos os dados deste projeto são \*\*sintéticos\*\* (gerados por código). Nenhum dado real de clientes foi utilizado.



\## O que o projeto faz



\- Gera uma base fictícia de 1000 contatos de atendimento

\- Calcula indicadores: total de contatos, tempo médio de resolução e nota média de satisfação

\- Exibe gráficos interativos por canal, categoria e mês



\## Tecnologias



Python, Pandas, Streamlit e Plotly.



\## Como rodar



```bash

python -m venv .venv

.venv\\Scripts\\activate

pip install -r requirements.txt

python src/gerar\_dados.py

streamlit run src/app.py

```



\## Próximos passos



\- Filtros por canal e categoria

\- Mais indicadores e análises

