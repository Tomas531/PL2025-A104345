# Trabalho de Casa 5 - Máquina de Vending

- **Nome**: Tomás Afonso Brito Oliveira  
- **N.º**: A104345  
- **Data**: 10/03/2025  

<p align="center">
  <img src="../foto.jpg" alt="Foto do aluno" style="width: 20%;">
</p>

Este trabalho de casa implementa uma máquina de venda automática utilizando Python e a biblioteca PLY (Python Lex-Yacc) para processar comandos.

## Funcionalidades

- **Listar produtos** disponíveis na máquina.
- **Inserir moedas** para adicionar ao saldo.
- **Selecionar um produto** para compra.
- **Sair da máquina** e receber o troco.

## Estrutura do Código

### Arquivo `stock.json`
O programa armazena o stock de produtos num ficheiro JSON (`stock.json`). Cada item no stock tem:
- `cod` - Código do produto.
- `nome` - Nome do produto.
- `quant` - Quantidade disponível.
- `preco` - Preço do produto em euros.

### Ficheiros principais

- **`VendingMachine`**: Classe que representa a máquina de venda automática.
- **`load_stock()`** e **`save_stock(stock)`**: Funções para carregar e guardar o stock no ficheiro JSON.
- **Métodos principais da classe `VendingMachine`**:
  - `listar()`: Lista os produtos disponíveis.
  - `inserir_moeda(moedas)`: Insere moedas e atualiza o saldo.
  - `selecionar(cod)`: Permite selecionar um produto, verificando o saldo e a disponibilidade.
  - `sair()`: Encerra a sessão e devolve o troco, se houver.
  - `calcular_troco()`: Calcula o troco a devolver.

### Implementação do Parser com PLY
O projeto utiliza **PLY (Python Lex-Yacc)** para processar comandos inseridos pelo utilizador.

#### Tokens
- `LISTAR`: Comando para listar produtos.
- `MOEDA`: Comando para inserir moedas.
- `SELECIONAR`: Comando para comprar um produto.
- `SAIR`: Comando para sair da máquina.
- `CODIGO`: Código de um produto.
- `MOEDAS`: Possiveis moedas a inserir.

#### Regras de Parsing
Cada comando é processado por regras de parsing:
- `comando : LISTAR` → Executa `vm.listar()`.
- `comando : MOEDA MOEDAS` → Executa `vm.inserir_moeda(moedas)`.
- `comando : SELECIONAR CODIGO` → Executa `vm.selecionar(p[2])`.
- `comando : SAIR` → Executa `vm.sair()`.

### Execução do Programa
Para executar a máquina de venda automática, basta rodar o script principal:
```sh
python tpc5.py
```
O utilizador pode então inserir comandos para com a máquina.

## Exemplo de Uso

```
>> MOEDA 1e
maq: Saldo = 1e0c
>> LISTAR
maq:
cod | nome | quantidade | preço
---------------------------------
A23 Ã¡gua 0.5L 7 0.7e
B45 sumo laranja 5 1.2e
C67 bolacha 0 0.5e
>> SELECIONAR A23
maq: Pode retirar o produto dispensado "Ã¡gua 0.5L"
maq: Saldo = 0e30c
>> LISTAR
maq:
cod | nome | quantidade | preço
---------------------------------
A23 Ã¡gua 0.5L 6 0.7e
B45 sumo laranja 5 1.2e
C67 bolacha 0 0.5e
>> SAIR
maq: Pode retirar o troco: 1x 20c, 1x 10c
maq: Até à próxima
```