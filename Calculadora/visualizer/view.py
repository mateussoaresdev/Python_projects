import io
import os
import pathlib

# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg
from PIL import Image  # pillow


def resize_image(imagepath, size=(100, 100)):
    image = Image.open(imagepath)
    image = image.resize(size)

    image_bytes = io.BytesIO()
    image.save(image_bytes, format="PNG")
    image_bytes = image_bytes.getvalue()

    return image_bytes


# Cria a janela principal
def create_main_window(title=None, theme="DarkTeal6"):
    # Definindo o nosso tema
    sg.theme(theme)

    parent_path = str(pathlib.Path(__file__).parent.resolve())
    image = "math.png"

    fullpath = os.path.join(parent_path, image)

    image = resize_image(fullpath)

    column_numbers = [
        [
            sg.Button("7", font=("Segoi UI", 20), size=(2, None)),
            sg.Button("8", font=("Segoi UI", 20), size=(2, None)),
            sg.Button("9", font=("Segoi UI", 20), size=(2, None)),
        ],
        [
            sg.Button("4", font=("Segoi UI", 20), size=(2, None)),
            sg.Button("5", font=("Segoi UI", 20), size=(2, None)),
            sg.Button("6", font=("Segoi UI", 20), size=(2, None)),
        ],
        [
            sg.Button("1", font=("Segoi UI", 20), size=(2, None)),
            sg.Button("2", font=("Segoi UI", 20), size=(2, None)),
            sg.Button("3", font=("Segoi UI", 20), size=(2, None)),
        ],
        [
            sg.Button("C", font=("Segoi UI", 20), size=(2, None)),
            sg.Button("0", font=("Segoi UI", 20), size=(2, None)),
            sg.Button(".", font=("Segoi UI", 20), size=(2, None)),
        ],
    ]

    column_operators = [
        [sg.Button("<<", font=("Segoi UI", 15), size=(2, None))],
        [sg.Button("/", font=("Segoi UI", 15), size=(2, None))],
        [sg.Button("*", font=("Segoi UI", 15), size=(2, None))],
        [sg.Button("-", font=("Segoi UI", 15), size=(2, None))],
        [sg.Button("+", font=("Segoi UI", 15), size=(2, None))],
        [sg.Button("=", font=("Segoi UI", 15), size=(2, None))],
    ]
    column_operators = [element_justification="center"]

    # Definindo o nosso layout
    layout = [
        [
            sg.Image(data=image, size=(100, 100)),
        ],
        [
            sg.Text("Calculadora 1990", font=("Calibri", 20, "bold")),
        ],
        [
            sg.Input(
                "0",
                size=(10, 30),
                font=("Segoi UI", 25),
                justification="right",
                readonly=True,
                text_color="black",
                key="-VALUE-",
            )
        ],
        [
            sg.Column(column_numbers, background_color="darkgrey", pad=(0, 0)),
            sg.Column(column_operators, background_color="grey", pad=(0, 5)),
        ],
    ]

    # Definindo o Título da janela
    if title is None:
        title = "Calculadora Antiga"
    else:
        title = title

    # Criar a janela e deixa ela finalizável
    window = sg.Window(title, layout, element_justification="center", finalize=True)

    # Retorna a nossa janela
    return window
