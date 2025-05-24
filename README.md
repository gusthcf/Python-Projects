# Decodificador de Textos Criptografados em Binario

Este repositorio contem dois programas desenvolvidos em Python para decodificar textos criptografados em formato binario utilizando:

- Cifra de Cesar
- Cifra de Substituicao

## Arquivos

- cesar.py — decodificador usando Cifra de Cesar (forca bruta sobre 26 shifts)
- substituicao.py — decodificador usando Cifra de Substituicao (heuristica com N-Gram)
- quadgrams.txt — dados estatisticos da lingua inglesa usados na decodificacao
- relatorio.pdf — explicacoes detalhadas sobre o funcionamento dos codigos e resultados
- desafioProposto.pdf - enunciado do desafio proposto
- requirements.txt — lista de dependencias do projeto

## Como executar

1. Instale as dependencias do projeto:
```bash
pip install -r requirements.txt
```

2. Execute um dos scripts:
```bash
python cesar.py
python substituicao.py
```

3. Siga as instrucoes no terminal para fornecer o texto em binario ou string.

## Relatorio

Todas as explicacoes detalhadas sobre a logica dos algoritmos, metodologia e resultados podem ser encontradas no arquivo:

- relatorio.pdf

