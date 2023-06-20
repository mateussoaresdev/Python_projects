# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

tasks = ["Limpar a casa", "Fazer exercícios de Python", "Formatar o PC"]


def strike(text):
    return "\u0336".join(text) + "\u0336"


def unstrike(text):
    return text.replace("\u0336", "")


# Recarrega a janela principal
def refresh_main_window(old_values):
    window = create_main_window()

    for key, value in old_values.items():
        window[key].update(value)

    return window


# Cria a janela principal
def create_main_window():
    global tasks

    # Definindo o nosso tema
    sg.theme("DarkTeal6")

    task_list = []

    for index, task in enumerate(tasks):
        task_list.append(
            [
                sg.Checkbox(
                    task,
                    key=f"-TASK{index}-",
                    enable_events=True,
                    font=("OpenSans", 12),
                ),
            ]
        )

    # Definindo o nosso layout
    layout = [
        [
            sg.Text("Minhas Tarefas", font=("OpenSans", 15)),
        ],
        *task_list,
        [
            sg.In(key="-NEWTASK-"),
            sg.Button("Adicionar", key="-ADD-"),
        ],
    ]

    # Definindo o Título da janela
    title = "Lista de Tarefas"

    # Criar a janela
    window = sg.Window(title, layout, finalize=True)

    # Retorna a nossa janela
    return window


# Definindo a janela inicial
window = create_main_window()

# Loop da Leitura da janela
while True:
    # Coletar Eventos e Valores atuais
    event, values = window.read()

    # Cancelar o loop ao fechar a janela
    if event == sg.WIN_CLOSED:
        break

    # Mostrar o evento e os valores
    print(event, "=>", values)

    if "-TASK" in event:
        # -TASK[id]-
        # [id]
        task_index = event.replace("-TASK", "").replace("-", "")  # 'id'
        task_index = int(task_index)  # id (int)
        task_text = tasks[task_index]

        if values[event]:
            new_text = strike(task_text)
        else:
            new_text = unstrike(task_text)

        tasks[task_index] = new_text
        window[event].update(text=new_text)


    if event == "-ADD-":
        window.close()
        tasks.append(values["-NEWTASK-"])
        window = refresh_main_window(values)


# Encerra a janela
window.close()
