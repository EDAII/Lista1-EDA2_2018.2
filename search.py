from random import *
import os

def checks_in_vector(vector, arr_len, bot, top):
    num = randint(bot, top)
    for element in vector:
        if element == num:
            num = checks_in_vector(vector, arr_len, bot, top)

    return num

def randomize_vector(bot, top, arr_len):
    vector = []
    for x in range (1, arr_len):
        value = checks_in_vector(vector, arr_len, bot, top)
        vector.append(value)
    return vector

def sequencial_search(vector, number):
    vectorsize = len(vector)
    for x in range(0, vectorsize):
        if vector[x] == number:
            return x

    return False

def binary_search(vector, n):
    middle = int(len(vector)/2)
    if vector:
        if vector[middle] == n:
            return middle
        elif n < vector[middle]:
            return binary_search(vector[:middle], n)
        else:
            return middle+binary_search(vector[middle:], n)
    else:
        return False


def binary_option():
    os.system('clear')
    arr_len = input("Insira o tamanho do vetor a ser criado: ")
    os.system('clear')
    bot = input("Insira o limite inferior do vetor a ser criado: ")
    os.system('clear')
    top = input("Insira o limite superior do vetor a ser criado: ")
    if (top - bot) < arr_len:
        print("Intervalo de numeros menor que o vetor")
        action = input("Digite 1 para tentar novamente: ")
        if action == 1:
            binary_option()
        else:
            show_menu()
    else:
        arr = sorted(randomize_vector(bot, top, arr_len))
        os.system('clear')
        print("Vetor criado: ")
        print(arr)
        num = input("Qual numero voce deseja procurar no vetor?: ")
        
        if binary_search(arr, num) == False:
            print("O numero nao foi encontrado no vetor\n")
        else:
            print("O numero " + str(num) + " esta na " + str(binary_search(arr, num)) + " posicao do vetor.\n")
        
        back = input("Digite qualquer coisa para voltar ao menu principal: ")
        if back != False:
            show_menu()


        
    

def sequencial_option():
    os.system('clear')
    arr_len = input("Insira o tamanho do vetor a ser criado: ")
    os.system('clear')
    bot = input("Insira o limite inferior do vetor a ser criado: ")
    os.system('clear')
    top = input("Insira o limite superior do vetor a ser criado: ")
    if (top - bot) < arr_len:
        print("Intervalo de numeros menor que o vetor")
        action = input("Digite 1 para tentar novamente: ")
        if action == 1:
            binary_option()
        else:
            show_menu()
    else:
        arr = sorted(randomize_vector(bot, top, arr_len))
        os.system('clear')
        print("Vetor criado: ")
        print(arr)
        num = input("Qual numero voce deseja procurar no vetor?: ")

        if sequencial_search(arr, num) == False:
            print("O numero nao foi encontrado no vetor\n")
        else:
            print("O numero " + str(num) + " esta na " + str(sequencial_search(arr, num)) + " posicao do vetor.\n")
            

        back = input("Digite qualquer coisa para voltar ao menu principal: ")
        if back != False:
            show_menu()

def show_menu():
    os.system('clear') 
    print("================================================\n")
    print("=============== Metodos de Busca ===============\n")
    print("================================================\n")

    print("           Selecione o Metodo de Busca          \n")
    print("   1)Busca Binaria\n")

    print("   2)Busca Sequencial\n")
    print("================================================\n")
    print("      Felipe Campos e Joao Egewarth, EDA2       \n")
    print("================================================\n")

    option = input("Insira uma opcao valida: ")
    
    if option == 1:
        binary_option()
    elif option == 2:
        sequencial_option()
    else:
        show_menu()



show_menu()


    