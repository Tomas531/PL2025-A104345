# Trabalho de Casa 4 - Analisador Léxico

- **Nome**: Tomás Afonso Brito Oliveira  
- **N.º**: A104345  
- **Data**: 6/03/2025  

<p align="center">
  <img src="../foto.jpg" alt="Foto do aluno" style="width: 20%;">
</p>

## Descrição
Este projeto contém um analisador léxico para uma linguagem de consulta baseada em SPARQL, utilizando a biblioteca `ply` (Python Lex-Yacc). O analisador reconhece tokens básicos como `SELECT`, `WHERE`, `LIMIT`, variáveis (`?var`), prefixos (`dbo:`, `foaf:`), strings, números e outros símbolos sintáticos.

## Funcionalidades
- Identifica palavras-chave (`SELECT`, `WHERE`, `LIMIT`, `a`).
- Reconhece variáveis SPARQL (`?variavel`).
- Deteta prefixos (`dbo:`, `foaf:`) usados em consultas.
- Lida com strings entre aspas (`"valor"@idioma`).
- Reconhece números inteiros (`1000`).
- Identifica identificadores genéricos (`MusicalArtist`, `artist`, `name`, `abstract`).
- Ignora espaços e tabulações.
- Trata comentários iniciados com `#`.
- Reporta erros de caracteres ilegais.

## Estrutura do Código
- Definição de tokens através de expressões regulares.
- Regras especiais para `VAR`, `PREFIX`, `STRING`, `NUMBER` e `IDENT`.
- Implementação de regras para ignorar espaços e contar novas linhas.
- Função `t_error` para lidar com caracteres inesperados.
- Execução do analisador léxico sobre uma consulta de exemplo.

## Exemplo de Entrada
```sparql
# DBPedia: obras de Chuck Berry

select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
```

## Exemplo de Saída
```plaintext
LexToken(COMENT,'# DBPedia: obras de Chuck Berry',1,1)
LexToken(SELECT,'select',1,34)
LexToken(VAR,'?nome',1,41)
LexToken(VAR,'?desc',1,47)
LexToken(WHERE,'where',1,53)
LexToken(LBRACE,'{',1,59)
LexToken(VAR,'?s',1,65)
LexToken(IDENT,'a',1,68)
LexToken(PREFIX,'dbo:',1,70)
LexToken(IDENT,'MusicalArtist',1,74)
LexToken(DOT,'.',1,87)
LexToken(VAR,'?s',1,93)
LexToken(PREFIX,'foaf:',1,96)
LexToken(IDENT,'name',1,101)
LexToken(STRING,'"Chuck Berry"@en',1,106)
LexToken(DOT,'.',1,123)
LexToken(VAR,'?w',1,129)
LexToken(PREFIX,'dbo:',1,132)
LexToken(IDENT,'artist',1,136)
LexToken(VAR,'?s',1,143)
LexToken(DOT,'.',1,145)
LexToken(VAR,'?w',1,151)
LexToken(PREFIX,'foaf:',1,154)
LexToken(IDENT,'name',1,159)
LexToken(VAR,'?nome',1,164)
LexToken(DOT,'.',1,169)
LexToken(VAR,'?w',1,175)
LexToken(PREFIX,'dbo:',1,178)
LexToken(IDENT,'abstract',1,182)
LexToken(VAR,'?desc',1,191)
LexToken(RBRACE,'}',1,197)
LexToken(LIMIT,'LIMIT',1,199)
LexToken(NUMBER,1000,1,205)
```

## Como Utilizar
1. Execute `python lexer.py`.
2. O analisador processará a consulta e imprimirá os tokens reconhecidos.
    
