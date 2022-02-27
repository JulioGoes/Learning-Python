import PySimpleGUI as sg

layout = [
    [sg.Text('My one-shot window.')],
    # [sg.InputText()],
    # [sg.Submit(), sg.Cancel()],
    [sg.Print('Testando', do_not_reroute_stdout=False)]
]

window = sg.Window('Window Title', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        window.close()

    text_input = values[0]
    sg.popup('You entered', text_input)
