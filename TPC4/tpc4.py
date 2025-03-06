import ply.lex as lex

tokens = (
    'COMENT', 'SELECT', 'WHERE', 'LIMIT', 'VAR', 'PREFIX',
    'DOT', 'COLON', 'LBRACE', 'RBRACE', 'STRING', 'NUMBER', 'A', 'IDENT'
)

t_SELECT = r'SELECT|select'
t_WHERE = r'WHERE|where'
t_LIMIT = r'LIMIT|limit'
t_STRING = r'"[^"]*"(@[a-zA-Z]+)?'
t_VAR = r'\?[a-zA-Z_]\w*'
t_PREFIX = r'[a-zA-Z]+:'
t_DOT = r'\.'
t_COLON = r':'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMENT = r'\#.*'
t_IDENT = r'[a-zA-Z]+'
t_A = r'a'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print(f"Carácter ilegal na linha {t.lineno}: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

query = """
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
"""

lexer.input(query)

while tok := lexer.token():
    print(tok)
