# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

from views.menu.menu import create_main_window
from views.registration.finish import create_finish_window
from views.registration.first import create_first_window
from views.registration.second import create_second_window
from views.registration.third import create_third_window
from views.visualizer.visualizer import create_visualizer_window

# Verifica se estamos executando esse arquivo como sendo o principal
if __name__ == "__main__":

    # Definindo a janela inicial
    window = create_main_window()

    current_window = "main"
    next_window = {
        "first": "second",
        "second": "third",
        "third": "finish",
        "finish": "main",
    }

    all_candidates = [
        ["Felipe", "01/01/2000", "5", "2007", "12000"],
        ["José", "09/02/2002", "2", "2021", "4500"],
        ["João", "01/01/1674", "10", "1992", "10000"],
    ]

    candidate = []

    # Loop da Leitura da janela
    while True:
        # Coletar Eventos e Valores atuais
        event, values = window.read()

        # Cancelar o loop ao fechar a janela
        if event == sg.WIN_CLOSED:
            break

        if event == "-REGISTER-":
            window.close()
            window = create_first_window()
            current_window = "first"

        elif event == "-SHOW-":
            window.close()
            window = create_visualizer_window(all_candidates)
            current_window = "visualizer"

        elif event == "-BACK-":
            window.close()
            window = create_main_window()
            current_window = "main"

        elif event == "-NEXT-":
            window.close()

            # Primeira Janela
            if next_window[current_window] == "second":
                candidate.append(values["-NAME-"])
                candidate.append(values["-BIRTHDAY-"])
                window = create_second_window()

            # Segunda Janela
            elif next_window[current_window] == "third":
                candidate.append(values["-LEVEL-"])
                candidate.append(values["-YEARPYTHON-"])
                window = create_third_window()

            # Terceira Janela
            elif next_window[current_window] == "finish":
                candidate.append(values["-SALARY-"])
                window = create_finish_window()

            # Janela Final
            else:
                all_candidates.append(candidate)
                candidate = []
                window = create_main_window()

            current_window = next_window[current_window]

        # Mostrar o evento e os valores
        print(event, "=>", values)

    # Encerra a janela
    window.close()
