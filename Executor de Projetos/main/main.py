import glob
import os
from threading import Thread

# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

from view import create_main_window


def run_file(file):
    os.system(f'python "{file}"')


path = ""
# Verifica se estamos executando esse arquivo como sendo o principal
if __name__ == "__main__":

    # Definindo a janela inicial
    window = create_main_window()

    # Loop da Leitura da janela
    while True:
        # Coletar Eventos e Valores atuais
        event, values = window.read()

        # Cancelar o loop ao fechar a janela
        if event == sg.WIN_CLOSED:
            break

        elif event == "-SEARCH-":
            path = values["-FOLDER-"]
            full_path = glob.escape(path) + "/**/main.py"
            all_projects = glob.glob(full_path, recursive=True)

            all_projects = [
                project.replace(path, "")[1:].replace("\main.py", "")
                for project in all_projects
            ]

            window["-LIST-"].update(values=all_projects)

        elif event == "-RUN-":
            project_name = values["-LIST-"][0]

            full_path = os.path.join(path, project_name, "main.py")

            with open(full_path, "r", encoding="utf-8") as file:
                content = file.read()
                window["-CODE-"].update(content)

            Thread(target=run_file, args=(full_path,)).start()

        # Mostrar o evento e os valores
        print(event, "=>", values)

    # Encerra a janela
    window.close()
