'''PySimpleGUI is a python GUI framework'''
import PySimpleGUI as sg


# create window - always the starting point for PySimpleGUI projects
# Takes title, layout as arguments
# Layout is a list (main window) of lists,
# each list a row (section of main window)
# optional arguments in the sublists create new columns in that row
# window['-TEXT1-'].update(values['-INPUT-']) (changes value of key)
# window['-TEXT1-'].update(visible = False) (hides the element)

layout = [
    [sg.Text('Lbs. to Oz.', enable_events = True, key = '-TEXT1-'), \
            sg.Spin(['item 1', 'item 2', 'item 3'], key = '-LBSTOOZ-')],
    # Button takes (Button text, Key for an ID)
    [sg.Text('Input your value: '), sg.Input(key = '-INPUT-')],
    [sg.Button('Convert', key = '-CONVERTBTN-'), sg.Text('0', key = '-OUTPUT-'),],
]

window = sg.Window('Conversion Application', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == '-CONVERTBTN-':
        value = int(values['-INPUT-'])
        window['-OUTPUT-'].update(str(value * 16))


    if event == '-TEXT1-':
        print('Text was pressed')

window.close()
