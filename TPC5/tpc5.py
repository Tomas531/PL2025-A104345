import json
import re
import ply.lex as lex
import ply.yacc as yacc
from datetime import datetime

STOCK_FILE = "stock.json"
COIN_VALUES = {"1e": 100, "50c": 50, "20c": 20, "10c": 10, "5c": 5, "2c": 2, "1c": 1}

# Carregar stock do ficheiro JSON
def load_stock():
    try:
        with open(STOCK_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Guardar stock no ficheiro JSON
def save_stock(stock):
    with open(STOCK_FILE, "w") as f:
        json.dump(stock, f, indent=4)

class VendingMachine:
    def __init__(self):
        self.stock = load_stock()
        self.saldo = 0
        print(f"maq: {datetime.today().date()}, Stock carregado, Estado atualizado.")
        print("maq: Bom dia. Estou disponível para atender o seu pedido.")

    def listar(self):
        print("maq:")
        print("cod | nome | quantidade | preço")
        print("---------------------------------")
        for item in self.stock:
            print(f"{item['cod']} {item['nome']} {item['quant']} {item['preco']}e")
    
    def inserir_moeda(self, moedas):
        total = 0
        for moeda in moedas:
            if moeda in COIN_VALUES:
                total += COIN_VALUES[moeda]
            else:
                print(f"maq: Moeda inválida {moeda}, ignorada.")
        self.saldo += total
        print(f"maq: Saldo = {self.saldo // 100}e{self.saldo % 100}c")
    
    def selecionar(self, cod):
        for item in self.stock:
            if item["cod"] == cod:
                if item["quant"] == 0:
                    print("maq: Produto esgotado.")
                    return
                preco_cents = int(item["preco"] * 100)
                if self.saldo >= preco_cents:
                    self.saldo -= preco_cents
                    item["quant"] -= 1
                    print(f"maq: Pode retirar o produto dispensado \"{item['nome']}\"")
                    print(f"maq: Saldo = {self.saldo // 100}e{self.saldo % 100}c")
                else:
                    print("maq: Saldo insuficiente para satisfazer o seu pedido")
                    print(f"maq: Saldo = {self.saldo // 100}e{self.saldo % 100}c; Pedido = {preco_cents // 100}e{preco_cents % 100}c")
                return
        print("maq: Produto inexistente.")
    
    def sair(self):
        troco = self.calcular_troco()
        if troco:
            print("maq: Pode retirar o troco:", ", ".join([f"{v}x {k}" for k, v in troco.items()]))
        print("maq: Até à próxima")
        save_stock(self.stock)
        exit()
    
    def calcular_troco(self):
        troco = {}
        saldo_temp = self.saldo
        for moeda, valor in sorted(COIN_VALUES.items(), key=lambda x: -x[1]):
            if saldo_temp >= valor:
                qtd = saldo_temp // valor
                troco[moeda] = qtd
                saldo_temp -= qtd * valor
        return troco

# Definição de tokens para PLY
tokens = ('LISTAR', 'MOEDA', 'SELECIONAR', 'SAIR', 'CODIGO', 'MOEDAS')

t_ignore = ' \t'

t_LISTAR = r'LISTAR'

t_MOEDA = r'MOEDA'

t_SELECIONAR = r'SELECIONAR'

t_SAIR = r'SAIR'

t_CODIGO = r'[A-Z][0-9]+'

t_MOEDAS = r'([1-9]?[0-9]c|1e)(,\s*([1-9]?[0-9]c|1e))*'
    
def t_error(t):
    print(f"Comando inválido: {t.value}")
    t.lexer.skip(len(t.value))

lexer = lex.lex()

def p_comando_listar(p):
    'comando : LISTAR'
    vm.listar()

def p_comando_moeda(p):
    'comando : MOEDA MOEDAS'
    moedas = re.findall(r'1e|[1-9]?[0-9]c', p[2])
    vm.inserir_moeda(moedas)

def p_comando_selecionar(p):
    'comando : SELECIONAR CODIGO'
    vm.selecionar(p[2])

def p_comando_sair(p):
    'comando : SAIR'
    vm.sair()

def p_error(p):
    print("Tenta de novo.")

parser = yacc.yacc()

if __name__ == "__main__":
    vm = VendingMachine()
    while True:
        try:
            command = input(">> ")
            parser.parse(command)
        except EOFError:
            break
