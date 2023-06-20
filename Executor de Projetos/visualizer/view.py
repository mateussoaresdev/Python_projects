import os
import pathlib

# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg


def frame_search():
    frame = [
        [
            sg.Text("Selecione a pasta com os projetos:"),
        ],
        [
            sg.Input(key="-FOLDER-", size=(70, None)),
            sg.FolderBrowse("Selecionar Pasta"),
        ],
        [
            sg.Button("Buscar Arquivos", key="-SEARCH-"),
        ],
    ]

    return frame


def frame_projects():
    frame = [
        [
            sg.Text("Selecione um projeto:"),
        ],
        [
            sg.Listbox(
                [],
                size=(85, 11),
                key="-LIST-",
            )
        ],
        [
            sg.Button("Rodar Código", key="-RUN-"),
        ],
    ]

    return frame


def frame_code():
    frame = [
        [
            sg.Multiline(
                "",
                size=(85, 22),
                key="-CODE-",
            )
        ]
    ]

    return frame


# Cria a janela principal
def create_main_window(title=None, theme="DarkTeal6"):
    # Definindo o nosso tema
    sg.theme(theme)

    column_left = [
        [
            sg.Frame("Buscar Projetos", frame_search()),
        ],
        [
            sg.Frame("Selecionar Projeto", frame_projects()),
        ],
    ]

    column_right = [
        [
            sg.Frame("Código", frame_code()),
        ],
    ]

    # Definindo o nosso layout
    layout = [
        [
            sg.Column(column_left),
            sg.Column(column_right),
        ]
    ]

    # Definindo o Título da janela
    if title is None:
        title = "Executador de Projetos"
    else:
        title = title

    parent_path = str(pathlib.Path(__file__).parent.resolve())
    icon_path = os.path.join(parent_path, "icon.ico")

    # Criar a janela e deixa ela finalizável
    window = sg.Window(title, layout, icon=icon_path, finalize=True)

    # Retorna a nossa janela
    return window
