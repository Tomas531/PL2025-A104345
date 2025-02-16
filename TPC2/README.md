# Trabalho de Casa 2 - Processamento de Obras Musicais em Python

- **Nome**: Tomás Afonso Brito Oliveira  
- **Nº**: A104345  
- **Data**: 2/11/2025

<p align="center">
  <img src="../foto.jpg" alt="Foto do aluno" style="width: 20%;">
</p>

## Descrição
Este projeto tem como objetivo processar um dataset de obras musicais armazenado no arquivo [`obras.csv`](./obras.csv), sem utilizar o módulo `csv` do Python. O [código](./tpc2.py) realiza a leitura, extração e organização dos dados para gerar os seguintes resultados:

1. **Lista ordenada alfabeticamente dos compositores musicais.**
2. **Distribuição das obras por período**, ou seja, quantas obras estão catalogadas em cada período.
3. **Dicionário em que cada período está associado a uma lista alfabética dos títulos das obras desse período.**

## Estrutura do Código
1. **Leitura do Arquivo CSV**
   - O arquivo [`obras.csv`](./obras.csv) é aberto em modo leitura com a codificação `utf-8`.
   - A primeira linha do arquivo (cabeçalho) é ignorada.
   - O conteúdo restante é lido e armazenado em uma string.

2. **Processamento dos Dados**
   - Utiliza-se uma expressão regular (`regex`) para extrair os campos do CSV.
   - Um conjunto (`set`) é utilizado para armazenar os compositores sem repetições.
   - Dois dicionários são criados:
     - [`dis_obras`](./tpc2.py): Contagem de obras por período.
     - [`periodo_obras`](./tpc2.py): Lista das obras associadas a cada período.

3. **Ordenação e Impressão dos Resultados**
   - Os compositores são ordenados alfabeticamente.
   - A contagem de obras por período é exibida.
   - As obras são listadas e organizadas por período.

## Saída Esperada
O código exibirá:

```
Compositores Musicais (ordenados alfabeticamente):
- Compositor A
- Compositor B
...

Distribuição das obras por período:
Período 1: X obra(s)
Período 2: Y obra(s)
...

Obras por período:

Período 1:
  - Obra 1
  - Obra 2
...
```

