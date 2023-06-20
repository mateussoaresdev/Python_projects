from datetime import datetime

# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg


# Cria a janela principal
def create_second_window(title=None, theme="DarkTeal6"):
    # Definindo o nosso tema
    sg.theme(theme)

    # Definindo o nosso layout
    layout = [
        [sg.Text("Qual seu nível de Python?")],
        [
            sg.Text("Iniciante"),
            sg.Slider((0, 10), orientation="horizontal", key="-LEVEL-"),
            sg.Text("Experiente"),
        ],
        [
            sg.Text("Em que ano inicou no Python: "),
            sg.Spin(
                list(
                    range(1991, datetime.now().year + 1),
                ),
                initial_value=2010,
                key="-YEARPYTHON-",
            ),
        ],
        [
            sg.Button("Avançar", size=(25, None), key="-NEXT-"),
        ],
        [
            sg.Text("Progresso:"),
            sg.ProgressBar(
                3,
                size=(35, 25),
                bar_color="green on lightgrey",
                key="-PROGRESS-",
            ),
        ],
    ]

    # Definindo o Título da janela
    if title is None:
        title = "Cadastro - Dados Profissionais"
    else:
        title = title

    # Criar a janela e deixa ela finalizável
    window = sg.Window(
        title,
        layout,
        element_justification="center",
        finalize=True,
    )

    window.find_element("-PROGRESS-").update(1)

    # Retorna a nossa janela
    return window
