# Trabalho de Casa 3 - Conversor de MarkDown para HTML

- **Nome**: Tomás Afonso Brito Oliveira  
- **Nº**: A104345  
- **Data**: 2/11/2025

<p align="center">
  <img src="../foto.jpg" alt="Foto do aluno" style="width: 20%;">
</p>

## Descrição
Neste [código](./tpc3.py) passamos por cada caso pedido em `markdown` e usando a biblioteca `regex` substituimos um de cada vez pelo seu equivalente em `html`. Estes são as substituições:

- **Cabeçalhos**: `# Texto`, `## Texto`, `### Texto`
- **Negrito**: `**Texto**`
- **Itálico**: `*Texto*`
- **Listas numeradas**: `1. Item`, `2. Item`, etc.
- **Links**: `[Texto](URL)`
- **Imagens**: `![Texto alternativo](URL)`


## Como Testar
Execute o ficheiro [`tpc3.py`](./tpc3.py) com o nome do ficheiro teste em `markdown`, [`teste.md`](./teste.md) como primeiro argumento e o nome do ficheiro html que o programa criara como segundo argumento.

```sh
python3 tpc3.py teste.md saida.html
```

Isso converterá o arquivo `teste.md` para `saida.html`.

## Exemplo de Entrada e Saída

### Entrada (`teste.md`):
```
# Título Principal
## Subtítulo
### Subsubtítulo

Este é um **exemplo** de texto em negrito.
Este é um *exemplo* de texto em itálico.

1. Primeiro item
2. Segundo item
3. Terceiro item

Veja mais em [Google](https://www.google.com).

Aqui uma imagem: ![Exemplo](https://www.exemplo.com/imagem.jpg)
```

### Saída (`saida.html`):
```html
<h1> Título Principal</h1>
<h2> Subtítulo</h2>
<h3> Subsubtítulo</h3>

Este é um <i>exemplo</i> de texto em negrito.
Este é um <b>exemplo</b> de texto em itálico.

<ol>
<li> Primeiro item</li>
<li> Segundo item</li>
<li> Terceiro item</li>
</ol>

Veja mais em <a href="https://www.google.com">Google</a>.

Aqui está uma imagem: <img src="https://www.exemplo.com/imagem.jpg" alt="Exemplo">
```


