'''PySimpleGUI is a python GUI framework'''
import PySimpleGUI as sg


# create window - always the starting point for PySimpleGUI projects
# Takes title, layout as arguments
# Layout is a list (main window) of lists,
# each list a row (section of main window)
# optional arguments in the sublists create new columns in that row
layout = [
    [sg.Text('Text'), sg.Spin(['item 1', 'item 2', 'item 3'])],
    # Button takes (Button text, Key for an ID)
    [sg.Button('Button', key = 'Button1')],
    [sg.Input()],
    [sg.Text('Hello'), sg.Button('Test Button', key = 'Button2')]
]

window = sg.Window('Conversion Application', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Button1':
        print('Button Pressed!')

    if event == 'Button2':
        print('The Test Button Pressed!')

window.close()
