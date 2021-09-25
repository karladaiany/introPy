# 1 - imports / bibliotecas
import pytest
# 2 - Classe

# 3 - Métodos e funções
#def = definition = definição
def print_hi(name):
    print(f'Oi, {name}')    #a partir do python3
    print('Oi, ' + name)    #antes do python3

def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento

def calcular_area_do_quadrado(lado):
    return lado ** 2

def calcular_area_do_triangulo(base, altura):
    return base * altura / 2

def contagem_progressiva(fim):
    for numero in range(fim):       #repetir tudo que esta dentro do bloco de 'numero' até o fim
        print(numero)               #exibir o número

def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        #contador = numero + 1
        #print(f'{contador} - {nome}')

        if numero < 9:
            print(f'00{numero + 1} - {nome}')
        elif numero < 99:
            print(f'0{numero + 1} - {nome}')
        else:
            print(f'{numero + 1} - {nome}')

def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM!')
        else:
            print('{:0>3}'.format(numero))


# estrutura de identificação / execução do script
if __name__ == '__main__':

    resposta = 'C'

    while resposta.upper() != 'Z':

        print('###################################')
        print('#                                 #')
        print('#   M E N U   D E   O P Ç Õ E S   #')
        print('#                                 #')
        print('###################################')
        print('#                                 #')
        print('#   1 - Olá mundo                 #')
        print('#   2 - Área do Retângulo         #')
        print('#   3 - Área do Quadrado          #')
        print('#   4 - Área do Triângulo         #')
        print('#   5 - Contagem Progressiva      #')
        print('#   6 - Apoiar Candidato          #')
        print('#   7 - Brincar de Plim!          #')
        print('#                                 #')
        print('#   Z - Sair                      #')
        print('#                                 #')
        print('###################################')

        resposta = input('Escolha sua opção: ')
        print(f'A sua escolha foi: {resposta}')

        if resposta.upper() != 'Z':
            if resposta == '1':
                print_hi('KarlaDaiany')
            elif resposta == '2':
                resultado = calcular_area_do_retangulo(3, 4)
                print(f'A área do retângulo é de {resultado}m²')
            elif resposta == '3':
                resultado = calcular_area_do_quadrado(5)
                print(f'A área do quadrado é de {resultado}m²')
            elif resposta == '4':
                resultado = calcular_area_do_triangulo(6,7)
                print(f'A área do triângulo é de {resultado}m²')
            elif resposta == '5':
                contagem_progressiva(8)
            elif resposta == '6':
                apoiar_candidato('Sabado',11)
            elif resposta == '7':
                brincar_de_plim(10)
            else:
                print('Opção Inválida. Escolha uma opção válida.')
        else:
            print('Você escolheu sair. Obrigada e Volte Sempre!')