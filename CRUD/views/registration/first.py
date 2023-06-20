# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg


# Cria a janela principal
def create_first_window(title=None, theme="DarkTeal6"):
    # Definindo o nosso tema
    sg.theme(theme)

    # Definindo o nosso layout
    layout = [
        [sg.Text("Nome Completo:"), sg.Input("", size=(50, None), key="-NAME-")],
        [
            sg.Text("Data de Nascimento:"),
            sg.In(size=(35, None), key="-BIRTHDAY-"),
            sg.CalendarButton("Selecionar", format="%d/%m/%Y"),
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
        title = "Cadastro - Dados Pessoais"
    else:
        title = title

    # Criar a janela e deixa ela finalizável
    window = sg.Window(
        title,
        layout,
        element_justification="center",
        finalize=True,
    )

    window.find_element("-PROGRESS-").update(0)

    # Retorna a nossa janela
    return window
