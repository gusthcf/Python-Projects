import ngram_score as ns
fitness = ns.ngram_score('quadgrams.txt')

BOLD = "\033[1m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
RESET = "\033[0m"

alfabeto = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def atribuiLetras(texto, alfabetoAleatorio):
    textoDecodificado = ''
    for letra in texto:
        if letra in alfabeto:
            posicao = alfabetoAleatorio.index(letra)
            textoDecodificado += alfabeto[posicao]
        else:
            textoDecodificado += letra
    return textoDecodificado


def decodifica(texto):
    maiorScore = float('-inf')
    frase = ''
    for i in range(0, 27, 1):
        letrasFinais = alfabeto[0:i]
        letrasIniciais = alfabeto[i:]
        alfabetoDeTraducao = letrasIniciais + letrasFinais
        textoDecodificado = atribuiLetras(texto, alfabetoDeTraducao)
        score = fitness.score(textoDecodificado)
        if score > maiorScore:
            maiorScore = score
            frase = textoDecodificado
    return frase


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
    # chamando a função que encontra o texto decodificado e imprimindo o texto
    textoDecodificado = decodifica(asciiString)
    print(BOLD + GREEN +
          f'O texto decodificado é:\n {textoDecodificado.lower()}\n' + RESET)
elif opcao == 'S':
    asciiString = str(
        input('Digite o texto para ser descriptografado: ')).upper()
    textoDecodificado = decodifica(asciiString)
    print(BOLD + GREEN +
          f'O texto decodificado é:\n {textoDecodificado.lower()}\n' + RESET)
else:
    print('Opção inválida!')
