# Trabalho de Casa 1

## Descrição
Este programa implementa a função `soma`, que processa uma string contendo caracteres alfabéticos, numéricos e símbolos especiais para calcular a soma dos números presentes no texto. A função pode ativar ou desativar a soma com base nas palavras-chave "on" e "off" encontradas na string.

## Funcionamento
1. A função percorre a string `texto` caracter por caracter.
2. Quando encontra a palavra "on" (independentemente de maiúsculas ou minúsculas), a soma é ativada.
3. Quando encontra a palavra "off" (independentemente de maiúsculas ou minúsculas), a soma é desativada.
4. Quando a soma está ativada, a função identifica e acumula os números encontrados na string.
5. Sempre que o caractere `=` é encontrado, a função imprime o valor acumulado até esse momento.
6. O processo continua até o fim da string.

