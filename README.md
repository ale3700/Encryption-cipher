# Cifra de César - Criptografia Simples

Este é um projeto simples de criptografia usando a **Cifra de César**, uma técnica clássica de criptografia de substituição.
O código permite que você digite uma mensagem e selecione uma chave para criptografá-la.

## Como funciona

A **Cifra de César** funciona deslocando cada letra de uma mensagem por um número fixo de posições no alfabeto, determinado por uma chave. Você pode escolher essa chave e ela determinará quantas posições cada letra da mensagem será deslocada:

- Com uma chave de valor positivo, as letras são deslocadas para a direita (alfabeto adiante).
- Com uma chave de valor negativo, as letras são deslocadas para a esquerda (alfabeto para trás).

**Nota**: Apenas letras serão deslocadas; espaços, números e outros caracteres serão mantidos sem alteração.

## Exemplo de Uso

### Entrada:
- Mensagem: `Hello World`
- Chave: `3`

### Saída:
- Mensagem criptografada: `Khoor Zruog`

### Entrada:
- Mensagem: `Hello World`
- Chave: `-3`

### Saída:
- Mensagem criptografada: `Ebiil Tloia`

## Como utilizar o código

### Pré-requisitos

- Ter o [Python 3](https://www.python.org/) instalado.

