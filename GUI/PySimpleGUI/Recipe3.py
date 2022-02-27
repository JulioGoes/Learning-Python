import PySimpleGUI as sg

layout = [
    [sg.Frame(title='My Frame', layout=[
        [sg.Text('Field:'), sg.Text('', key='-KEY NAME-', size=(10, 0))]])],
    [sg.Button('Go')] 
]

window = sg.Window(title='Name', layout=layout).finalize()

window['-KEY NAME-'].update('No value set')

# MAIN LOOP
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Go':
        window['-KEY NAME-'].update('Hello World!')

window.close()