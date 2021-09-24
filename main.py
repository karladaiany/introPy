# import

# metodos / funções

#def = definition = definição
def print_hi(name):
    print(f'Hi, {name}')

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
    print_hi('KarlaDaiany')

# chamar a função de cálculo da área do retângulo
    resultado = calcular_area_do_retangulo(3,4)
    print(f'A área do retâgulo é de {resultado}m²')

# chamar a função de cálculo da área do quadrado
    resultado = calcular_area_do_quadrado(5)
    print(f'A área do quadrado é de {resultado}m²')

# chamar a função de cálculo da área do triângulo
    resultado = calcular_area_do_triangulo(6,7)
    print(f'A área do triângulo é de {resultado}m²')

# chamar a função de contagem progressiva
    contagem_progressiva(10)

# chamar a função de apoiar candidato
    apoiar_candidato('Faker', 100)