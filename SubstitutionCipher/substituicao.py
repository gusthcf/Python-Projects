import random
import os
import ngram_score as ns
fitness = ns.ngram_score('quadgrams.txt')

BOLD = "\033[1m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
RESET = "\033[0m"

alfabeto = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


# função que recebe um texto e um alfabeto desordenado e faz a correspondencia com o alfabeto normal
def atribuiLetras(texto, alfabetoAleatorio):
    textoDecodificado = ''
    for letra in texto:
        if letra in alfabeto:
            posicao = alfabetoAleatorio.index(letra)
            textoDecodificado += alfabeto[posicao]
        else:
            textoDecodificado += letra
    return textoDecodificado


# função realiza x trocas de letras em um alfabeto recebido como parâmetro
def criarAlfabetoParecido(alfabetoAtual, trocas):
    alfabetoParecido = alfabetoAtual.copy()
    for i in range(trocas):
        letra1 = random.sample(alfabetoParecido, 1)[0]
        indexLetra1 = alfabetoParecido.index(letra1)
        letra2 = random.sample(alfabetoParecido, 1)[0]
        indexLetra2 = alfabetoParecido.index(letra2)
        alfabetoParecido[indexLetra1] = letra2
        alfabetoParecido[indexLetra2] = letra1
    return alfabetoParecido


# função que encontra o melhor texto e o retorna
def decodifica(texto):
    # criando as variaveis para guardar um texto atual e um melhor texto
    alfabetoAtual = alfabeto.copy()
    random.shuffle(alfabetoAtual)
    textoAtual = atribuiLetras(texto, alfabetoAtual)
    melhorTexto = textoAtual
    scoreAtual = fitness.score(melhorTexto)
    melhorScore = scoreAtual
    iteracaoMelhorScore = 0
    iteracoesIniciais = 1000
    iteracoesSemMelhoria = 0
    numeroIteracoes = 30000
    for i in range(0, numeroIteracoes, 1):
        if i < iteracoesIniciais:
            trocas = random.randint(3, 5)
        else:
            trocas = random.randint(1, 3)
        # saindo do ponto ótimo caso hajam mais de 2000 iterações iguais embaralhamos o alfabeto novamente e tentamos achar outro melhor texto
        if iteracoesSemMelhoria == 2000:
            print(BOLD + YELLOW +
                  f'2000 iterações sem melhoria, algoritmo entrou em zona ótima. Texto atual reiniciado.\n' + RESET)
            random.shuffle(alfabetoAtual)
            textoAtual = atribuiLetras(texto, alfabetoAtual)
            scoreAtual = fitness.score(textoAtual)
            iteracoesSemMelhoria = 0
        # criando um alfabeto parecido com o atual, trocando algumas letras
        alfabetoParecido = criarAlfabetoParecido(alfabetoAtual, trocas)
        textoParecido = atribuiLetras(texto, alfabetoParecido)
        scoreAlfabetoParecido = fitness.score(textoParecido)
        # se o alfabeto parecido for melhor que o atual, troca o atual pelo parecido
        if scoreAlfabetoParecido > scoreAtual:
            iteracoesSemMelhoria = 0
            alfabetoAtual = alfabetoParecido.copy()
            textoAtual = textoParecido
            scoreAtual = scoreAlfabetoParecido
        else:
            iteracoesSemMelhoria += 1
        # se o alfabeto atual for melhor que o melhor alfabeto, troca o melhor alfabeto pelo atual
        if scoreAtual > melhorScore:
            melhorScore = scoreAtual
            melhorTexto = textoAtual
            iteracaoMelhorScore = i
        # printando o melhor texto a cada 1000 iterações
        if i % 1000 == 0:
            print(BOLD + YELLOW + f'iteração atual: {i}' + RESET)
            print(BOLD + YELLOW + 'melhor texto:' + RESET)
            print(f'{melhorTexto.lower()}\n')
    print(BOLD + BLUE +
          f'O melhor texto foi encontrado na iteração {iteracaoMelhorScore}!' + RESET)
    return melhorTexto


# na main, recebemos o texto em binario ou string
opcao = str(input(
    'Digite B para entrada em binário ou S para entrada em string: ')).upper()
# caso seja recebido em binário, fazemos a conversao para inteiro e depois para string
if opcao == 'B':
    texto = str(input('Digite o texto em binário para ser descriptografado: '))
    textoLista = texto.split()
    asciiLista = []
    for binario in textoLista:
        asciiLista.append(chr(int(binario, 2)))
    asciiString = ''.join(asciiLista).upper()
    os.system('cls' if os.name == 'nt' else 'clear')
    # chamando a função que encontra o texto decodificado e imprimindo o texto
    textoDecodificado = decodifica(asciiString)
    print(BOLD + BLUE + f'O texto decodificado é:' + RESET)
    print(BOLD + GREEN + textoDecodificado.lower() + '\n' + RESET)
elif opcao == 'S':
    asciiString = str(
        input('Digite o texto para ser descriptografado: ')).upper()
    os.system('cls' if os.name == 'nt' else 'clear')
    textoDecodificado = decodifica(asciiString)
    print(BOLD + BLUE + f'O texto decodificado é:' + RESET)
    print(BOLD + GREEN + textoDecodificado.lower() + '\n' + RESET)
else:
    print('Opção inválida!')
