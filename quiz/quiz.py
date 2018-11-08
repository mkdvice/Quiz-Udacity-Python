# -*- coding: utf-8 -*-

''' Programa escrito em Python 3.6 '''

__author__= "@Ezequiel_Alexandre"

# IPND Projeto Final

# Perguntas para o level fácil
pergun_facil = 'A capital do Brasil é __1__ fica no estado de __2__ cuja a capital é __3__ conhecida como a cidade do __4__'

# Respostas para o level fácil
resp_facil = ['brasilia', 'goias', 'goiania', 'sertanejo']

# Perguntas para o level médio
pergun_med = 'A revolução industrial teve inicio no século __1__ , ela começou na __2__ e mudou a vida da __3__ com suas __4__'

# Respostas para level médio
resp_med = ['xviii', 'inglaterra', 'humanidade', 'maquinas']

# Perguntas para level difícil
pergun_dif = 'O Tratado de Tordesilhas que "dividia" o mundo entre as duas potências da época, __1__' \
             'e Espanha. A chegada dos holandeses à __2__ e à Nova Zelândia o correu no ano de ' \
             '1606. A Nova Zelândia é conhecida pelo seus __3__ e por ter uma grande população de __4__ '

# Respostas para level difícil
resp_dif = ['portugal', 'australia', 'esportes radicais', 'ovelhas']

# Lista de cada pergunta em números para cada level
perguntas = ["__1__", "__2__","__3__","__4__"]

# Irá perguntar o level do jogador
def levels():
    print('Bem vindo! Esse é game de perguntas sobre história e geografia\nPara selecionar o nível das perguntas ')

    nome_level = input('Escreva: fácil, médio ou difícil\n').lower() # Entrada do level, e converte para letras minusculas

    if nome_level == 'fácil' or nome_level == 'facil': # Será definido o level fácil
        verif_quest(pergun_facil, perguntas, resp_facil)
    elif nome_level == 'médio' or nome_level == 'medio': # Será definido o level médio
            verif_quest(pergun_med, perguntas, resp_med)
    elif nome_level == 'difícil' or nome_level == 'dificil': # Será definido o level difícil
            verif_quest(pergun_dif, perguntas, resp_dif)
    else:
        print('Por Favor, escolha somente fácil, médio ou difícil')
    print(levels)

# Inicializa o quiz, verifica as respostas e limites de entradas
def verif_quest(quiz, vazios, respostas):
    print(quiz)
    for conta_vazios in range(0,len(vazios)):
        entrada_resposta = input('Qual é resposta da lacuna ' + vazios[conta_vazios] + '?')
        tentativas = 1
        max_tantativas = 4
        while entrada_resposta.lower() != respostas[conta_vazios]:
            tentativas += 1
            entrada_resposta = input('Errou! Vamos novamente. Qual é resposta da lacuna ' + vazios[conta_vazios] + '?')
            if tentativas == max_tantativas:
                print('Infelizmente você falhou no teste. Tente novamente!')
                levels()

        else:
            quiz = quiz.replace(vazios[conta_vazios], respostas[conta_vazios])
            print('Acertou! ' + quiz)

    if len(vazios) == len(respostas):
        print('Parabéns você é fera, tente outro level!')
        levels()

levels()


