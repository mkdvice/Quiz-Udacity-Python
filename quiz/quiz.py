# -*- coding: utf-8 -*-

'''Programa escrito em Python 3.6'''

__author__ = "@Ezequiel_Alexandre"

# IPND Projeto Final

import time

#Perguntas e respostas de nível fácil
pergun_facil = 'A capital do Brasil é __1__ fica no estado de __2__ cuja a capital é __3__ conhecida como a cidade do __4__'
resp_facil = ['BRASILIA', 'GOIÁS', 'GOIÂNIA', 'SERTANEJO']

#Perguntas e respostas de nível médio
pergun_med = 'A revolução industrial teve inicio no século __1__ , ela começou na __2__ e mudou a vida da __3__ com suas __4__'
resp_med = ['XVIII', 'INGLATERRA', 'HUMANIDADE', 'MÁQUINAS']

#Perguntas e respostas de nível difícil
pergun_dif = 'O Tratado de Tordesilhas que "dividia" o mundo entre as duas potências da época, __1__' \
             'e Espanha. A chegada dos holandeses à __2__ e à Nova Zelândia o correu no ano de ' \
             '1606. A Nova Zelândia é conhecida pelo seus __3__ e por ter uma grande população de __4__ '
resp_dif = ['PORTUGAL', 'AUSTRÁLIA', 'ESPORTES RADICAIS', 'OVELHAS']

esp_vazios = ['__1__', '__2__', '__3__', '__4__'] # Os espaços vazios do quiz

index = 0

def questionario(pergunta_quiz, resposta_quiz, index):
    '''Essa função servirá para preencher os campos do quiz __1__, __2__, __3__ e __4__ '''

    if index == 0: # index igual a 0, corresponde ao primeiro número da lista
        subtr_palavras1 = []
        lista_split = pergunta_quiz.split(' ') # Para dividir as palavras para entrar na lista_split
        for item in lista_split: # para pegar os itens da lista_split
            if item == esp_vazios[0]: # Se o item for igual a resposta __1__
                subtr_palavras1.append(resposta_quiz[0]) # Irá adicionar a palavra na primeira lacuna do quiz
            else: # para que possa passar para pergunta 2
                subtr_palavras1.append(item) # adicionando a entrada na 1ª lacuna
        prm_preench = ' '.join(subtr_palavras1) # Irá criar uma string unica na primeira lacuna
        index = index + 1 # adicinando o ponto para que se passa para segunda palavra
        verif_questao(prm_preench, resposta_quiz, esp_vazios, index)

    elif index == 1: # irá para __2__
        subtr_palavras2 = []
        lista_split = pergunta_quiz.split(' ')
        for item in lista_split:
            if item == esp_vazios[0]: # mostra a respota __1__
                subtr_palavras2.append(resposta_quiz[0])
            elif item == esp_vazios[1]: # irá mostrar a resposta  __2__
                subtr_palavras2.append(resposta_quiz[1])
            else:
                subtr_palavras2.append(item)
        seg_preench = ' '.join(subtr_palavras2)
        index = index + 1
        verif_questao(seg_preench, resposta_quiz, esp_vazios, index)

    elif index == 2: # irá para __3__
        subtr_palavras3 = []
        lista_split = pergunta_quiz.split(' ')
        for item in lista_split:
            if item == esp_vazios[0]: # mostra resposta __1__
                subtr_palavras3.append(resposta_quiz[0])
            elif item == esp_vazios[1]: # mostra resposta __2__
                subtr_palavras3.append(resposta_quiz[1])
            elif item == esp_vazios[2]: # irá mostrar resposta __3__
                subtr_palavras3.append(resposta_quiz[2])
            else:
                subtr_palavras3.append(item)
        tres_preench = ' '.join(subtr_palavras3)
        index = index + 1
        verif_questao(tres_preench, resposta_quiz, esp_vazios, index)

    else: # Irá para __4__
        complet_lacuna = []
        lista_split = pergunta_quiz.split(' ')
        for item in lista_split:
            if item == esp_vazios[0]: # mostra resposta __1__
                complet_lacuna.append(resposta_quiz[0])
            if item == esp_vazios[1]: # mostra resposta __2__
                complet_lacuna.append(resposta_quiz[1])
            if item == esp_vazios[2]: # mostra resposta __3__
                complet_lacuna.append(resposta_quiz[2])
            if item == esp_vazios[3]: # Ira mostrar a resposta __4__
                complet_lacuna.append(resposta_quiz[3])
            else:
                complet_lacuna.append(item)

        completo = ' '.join(complet_lacuna)

        print('\n')
        print(completo)
        print('\n')
        print('Parabéns você terminou!')
        exit()

def verif_questao(pergunta_quiz, resposta_quiz, esp_vazios, index):
    # Irá verificar os inputs do user

    pergunta_quiz = pergunta_quiz # tranformando em variavel interna
    resposta_quiz = resposta_quiz # tranformando em variavel interna
    index = index # tranformando em variavel interna

    tentativas = 3
    print(index)
    print('Por favor leia, e preencha as lacunas vázias\n')
    print(pergunta_quiz)
    print('\nVocê tem 4 tentativas para acertar\n')
    print('Preencha', esp_vazios[index], 'Por favor\n')

    time.sleep(2) # tempo para o programa mostrar o resultado
    resposta = input() # Entrada da resposta
    resposta = resposta.upper() # Transfomando a resposta em String maiúscula
    if resposta == resposta_quiz[index]: # Resposta certa
        time.sleep(2)
        print('Parabéns!!!\n')
        questionario(pergunta_quiz, resposta_quiz, index)

    else: # Se a resposta for errada
        time.sleep(2)
        print('Você respondeu errado! Ainda restam ', tentativas, 'tentativas')
        while tentativas > 0: # A msg irá aparecer enquanto as tentativas não chegarem a zero
            print('Preencha', esp_vazios[index], ' Por favor\n')
            resposta = input()
            resposta = resposta.upper()
            if resposta == resposta_quiz[index]:
                time.sleep(2)
                print('Parabéns!!!\n')
                questionario(pergunta_quiz, resposta_quiz, index)
            else:
                tentativas = tentativas - 1 # Para mostrar que as tentativas estão acabando
                print('Você respondeu errado! Ainda restam ', tentativas, 'tentativas')
        print('Até mais!')
        exit() # fecha o programa

print('''======================================================
+ +       BEM VINDO AO GAME DAS PERGUNTAS          + +
======================================================\n''')

nome = input('Olá, qual é o seu nome? ') # Entrada do nome do user

print('Bem vindo', nome,'!', 'Esse é uma game de perguntas sobre história e geografia')

levels = range(0,5) # Para escolher o número da dificuldade

print('\nEscolha nível do jogo digitando um número de 1 à 3, ou 0 e 4 para sair do jogo\n1 = Difícil\n2 = Médio\n3 = Fácil\n0-4 = Sair ')

level = input('Digite a dificuldade desejada: ') # Entrada da dificuldade pelo user
level = int(level)

while level not in levels: # caso o user insira um número fora da dificuldade
    print('\nEscolha nível do jogo digitando um número de 1 à 3, ou 0 e 4 para sair do jogo\n1 = Difícil\n2 = Médio\n3 = Fácil\n0-4 = Sair')
    level = input('Digite a dificuldade desejada: ') # entrada da dificuldade
    level = int(level)

if level == 1: # Se for level díficil
    verif_questao(pergun_dif, resp_dif, esp_vazios, 0) # executa nível díficil

if level == 2: # Se for level médio
    verif_questao(pergun_med, resp_med, esp_vazios, 0) # executa nível médio

if level == 3: # Se for level fácil
    verif_questao(pergun_facil, resp_facil, esp_vazios, 0) # executa nível fácil

if level == 0 or 4: # Para sair do programa
    quit()

'''Sites usados para consultas:
https://www.youtube.com/user/cursosemvideo
https://pt.stackoverflow.com/questions/121920/input-ou-raw-input/121922
https://wiki.python.org.br/ManipulandoStringsComPython
https://www.tutorialspoint.com/python/string_upper.htm'''