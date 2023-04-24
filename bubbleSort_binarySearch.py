# UM JOGO DE ADIVINHAÇÃO, SÓ QUE DE MANEIRA OTIMIZADA
# primeiro peça uma lista com uma quantidade de numeros aleatorios
# peça um numero pro usuario para adivinhar se ele esta ou nao na lista
# ordene-os e busque se o numero esta na lista de forma alternada
# importe o modulo cProfile, e rode o codigo cProfile.run(function()) para ver a velocidade e consumo de memoria da função
import random
size_list = int(input("How many numbers in the list do u want? "))
min_max = input("Type the min and max of the list: ")
try:
    values = min_max.split(',')
    min, max = int(values[0]), int(values[1])
except (ValueError, IndexError):
    print("The min and max number must be separated by colon (,)")
    min_max = input("Type the min and max of the list: ")

value = input("which value do you want to search for? ")

# TODO: tem que implementar a distribuição de gauss no código e estudar sobre
_random_list = [random.randint(min, max) for i in range(size_list)]

def sorted(_random_list) -> list:
    n = size_list - 1
    for j in range(n-1):
        for i in range(n-1):
           if (_random_list[i] > _random_list[i+1]):
                _random_list[i], _random_list[i+1] = _random_list[i+1], _random_list[i]
    return print(_random_list[:])    

sorted(_random_list=_random_list)

# TODO: Já foi implementado o sistema de ordenação, mas ele é lento, ele é O(N²), ter que substituir para outro
# TODO: Fazer a busca binária e procurar pelo número
# TODO: Medir a velocidade do código e o uso de memória
# TODO: Fazer a interface para o código usando PyQT