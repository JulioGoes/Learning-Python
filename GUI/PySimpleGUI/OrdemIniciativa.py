import PySimpleGUI as sg
from typing import List
import operator


def ordena(nome, iniciativa):
    dici = {}

    for i in range(len(nome)):
        dici.update({nome[i]: iniciativa[i]})

    dicionario_ordenado = dict(sorted(dici.items(),
                                      key=operator.itemgetter(1),
                                      reverse=True))

    # Retorna o dicionário ordenado.
    print(dicionario_ordenado)
    lista = []
    for item in dicionario_ordenado.items():
        nome = item[0]
        num = item[1]
        teste = list((num, nome))
        lista.append(tuple(teste))
    return lista


def mostraSegundaTela(nome, iniciativa):
    lista = ordena(nome, iniciativa)
    i = 0
    layout2 = [
        [sg.Text('Ordem da Iniciativa')],
        [sg.Listbox(values=lista, enable_events=False, size=(20, 10),
                    expand_y=True, key='-KEY NAME-', text_color='yellow',
                    no_scrollbar=True)],
        [sg.Text('Turno')],
        [sg.Multiline(size=(20, 1), key='-OUTPUT-', no_scrollbar=True)],
        [sg.Button('Iniciar'), sg.Button('Próximo')]
    ]
    window2 = sg.Window('Ordem de Iniciativa', layout2)

    while True:

        event, values = window2.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Próximo':
            window2['-OUTPUT-'].update(lista[i][1])
            i += 1
            if (len(lista) == i):
                i = 0
        if event == 'Iniciar':
            window2['-OUTPUT-'].update(lista[i][1])
            i += 1

    window2.close()


sg.theme('DarkAmber')
layout = [
    [sg.Text('Nome', size=(10, None)), sg.InputText(size=(25, 0),
                                                    do_not_clear=False)],
    [sg.Text('Iniciativa', size=(10, None)), sg.InputText(size=(25, 0),
                                                          do_not_clear=False)],
    [sg.Button('Adicionar', expand_x=1), sg.Button('Finalizar', expand_x=1)]
]

window = sg.Window('Ordem de Iniciativa', layout)

nome: List = []
iniciativa: List = []

while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif values[0] == '0' or event == 'Finalizar':
        window.close()
        mostraSegundaTela(nome, iniciativa)
        break
    elif event == 'Adicionar':
        nome.append(values[0].title())
        iniciativa.append(str(values[1]).rjust(2, '0'))

window.close()
