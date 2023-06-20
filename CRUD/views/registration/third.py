# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg


# Cria a janela principal
def create_third_window(title=None, theme="DarkTeal6"):
    # Definindo o nosso tema
    sg.theme(theme)

    # Definindo o nosso layout
    layout = [
        [
            sg.Text("Salário Desejado:"),
            sg.Input("", size=(50, None), key="-SALARY-"),
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
        title = "Cadastro - Dados Salariais"
    else:
        title = title

    # Criar a janela e deixa ela finalizável
    window = sg.Window(
        title,
        layout,
        element_justification="center",
        finalize=True,
    )

    window.find_element("-PROGRESS-").update(2)

    # Retorna a nossa janela
    return window
