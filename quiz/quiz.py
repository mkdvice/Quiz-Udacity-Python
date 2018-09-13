# -*- coding: utf-8 -*-

__author__ = "@Ezequiel_Alexandre"

# IPND Projeto Final

import time

#Perguntas e respostas de nível fácil
pergun_facil = 'A capital do Brasil é __1__ fica no estado de __2__ cuja a capital é __3__ conhecida como a cidade' \
               'do __4__'
resp_facil = ['Brasilia', 'Goiás', 'Goiania', 'sertanejo']

#Perguntas e respostas de nível médio
pergun_med = 'A revolução industrial teve inicio no século __1__, ela começou na __2__,' \
             'e mudou a vida da __3__ com suas __4__'
resp_med = ['XXIII', 'Inglaterra', 'humanidade', 'máquinas']

#Perguntas e respostas de nível difícil
pergun_dif = 'O Tratado de Tordesilhas que "dividia" o mundo entre as duas potências da época, __1__' \
             ' e Espanha. A chegada dos holandeses à Austrália e à Nova Zelândia o correu no ano de ' \
             '__2__. A Nova Zelândia é conhecida pelo seus __3__ e por ter uma grande população de __4__ '
resp_dif = ['Portugal', '1606', 'esportes radicais', 'ovelhas']

esp_vazios = ['__1__', '__2__', '__3__', '__4__'] # Os espaços vazios do quiz

index = 0

print('''======================================================
+ +       BEM VINDO AO GAME DAS PERGUNTAS          + +
======================================================\n''')

nome = input('Olá, qual é o seu nome? ')

print('Bem vindo', nome,'!', 'Esse é uma game de perguntas sobre história e geografia')


def questionario(pergunta_quiz, resposta_quiz, index):
    '''Essa função servirá para preencher os campos do quiz __1__, __2__ e __3__ '''

    if index == 0: # ocupar_brn igual a 0, corresponde ao primeiro número da lista
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

    elif index == 1:
        subtr_palavras2 = []
        lista_split = pergunta_quiz.split(' ')
        for item in lista_split:
            if item == esp_vazios[0]:
                subtr_palavras2.append(resposta_quiz[0])
            elif item == esp_vazios[1]:
                subtr_palavras2.append(resposta_quiz[1])
            else:
                subtr_palavras2.append(item)
            seg_preench = ' '.join(subtr_palavras2)
            index = index + 1
            verif_questao(seg_preench, resposta_quiz, esp_vazios, index)




def verif_questao (pergunta_quiz, resposta_quiz, esp_vazios, index):
