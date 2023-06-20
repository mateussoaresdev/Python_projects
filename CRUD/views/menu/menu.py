# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg


# Cria a janela principal
def create_main_window(title=None, theme="DarkTeal6"):
    # Definindo o nosso tema
    sg.theme(theme)

    # Definindo o nosso layout
    layout = [
        [
            sg.Text(
                "VAGAS - ACME Tecnologia INC. - 2021",
                font=("Calibri", 18),
            ),
        ],
        [
            sg.Button("Visualizar Todos os Candidatos", key="-SHOW-"),
        ],
        [sg.Button("Cadastrar Novo Candidado", key="-REGISTER-")],
    ]

    # Definindo o Título da janela
    if title is None:
        title = "Recrutamento ACME"
    else:
        title = title

    # Criar a janela e deixa ela finalizável
    window = sg.Window(
        title,
        layout,
        element_justification="center",
        finalize=True,
    )

    # Retorna a nossa janela
    return window
