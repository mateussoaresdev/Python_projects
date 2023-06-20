# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg


# Cria a janela principal
def create_font_popup(title=None, content=None):

    # Definindo o nosso layout
    layout = [
        [
            sg.Text(content),
        ],
        [sg.Input(key="-VALUE-")],
        [sg.Button("OK"), sg.Button("Cancel")],
    ]

    # Definindo o Título da janela
    title = title

    # Criar a popup e lê os eventos/valores dela
    event, values = sg.Window(title, layout, finalize=True).read(close=True)

    # Retorna o valor da popup
    if event == "OK":
        return values["-VALUE-"]
    else:
        return False


# Cria a janela principal
def popup_combo(values, default_value=None, title=None, content=None):

    if default_value is not None:
        if default_value in values:
            default_index = values.index(default_value)
            default_value = values[default_index]
        else:
            default_value = default_value

    # Definindo o nosso layout
    layout = [
        [
            sg.Text(content),
        ],
        [
            sg.Combo(values, default_value, key="-VALUE-"),
        ],
        [
            sg.Button("OK"),
            sg.Button("Cancel"),
        ],
    ]

    # Definindo o Título da janela
    title = title

    # Criar a popup e lê os eventos/valores dela
    popup_event, popup_values = sg.Window(title, layout, finalize=True).read(close=True)

    # Retorna o valor da popup
    if popup_event == "OK":
        return popup_values["-VALUE-"]
    else:
        return False
