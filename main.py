import os

# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

from popups import create_font_popup, popup_combo
from view import create_main_window

current_theme = "DarkTeal6"
font_family = "Arial"
font_size = 10
file_name = "Novo Arquivo"
full_file_name = file_name
chars = 0
lines = 1


def update_status_bar(content):
    chars = len(content.strip().replace("\n", ""))
    lines = len(content.strip().split("\n"))

    status_bar_text = f"Arquivo Atual: {full_file_name} | O arquivo tem um total de {chars} caracteres e {lines} linhas | Você está usando o ByEditor de Texto 2.0.0"

    window["-STATUSBAR-"].update(status_bar_text)


def refresh_window():
    global window

    content = values["-CONTENT-"]
    size = window.size
    location = window.current_location()
    window.close()

    window = create_main_window(
        title=f"ByEditor de Texto 2.0.0 - {file_name}",
        theme=current_theme,
        size=size,
        location=location,
        font=(font_family, font_size),
    )

    window["-CONTENT-"].update(content)
    update_status_bar(content)


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

        elif "::new" in event:
            confirm = sg.popup(
                "Você tem certeza?", custom_text=("Sim", "Não"), title="Atenção!"
            )

            if confirm == "Sim":
                window["-CONTENT-"].update("")
                update_status_bar("")

        elif "::open" in event:
            file_path = sg.popup_get_file("Selecione um arquivo para abrir")

            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            file_name = os.path.basename(file_path)
            full_file_name = file_path
            refresh_window()

            window["-CONTENT-"].update(content)
            update_status_bar(content)

        elif "::save" in event:
            file_path = sg.popup_get_file("Como deseja salvar o arquivo?", save_as=True)

            with open(file_path, "w", encoding="utf-8") as file:
                file.write(values["-CONTENT-"])

            file_name = os.path.basename(file_path)
            full_file_name = file_path
            refresh_window()

        elif "::credits" in event:
            sg.popup_no_buttons(
                "Créditos: ByLearn \nInstagram: @bylearn \nSite: bylearn.com.br"
            )

        elif "::version" in event:
            sg.popup("Versão: 2.0.0")

        elif "::size" in event:
            font_size = create_font_popup(
                "Tamanho da Fonte", "Insira o tamanho da fonte"
            )
            refresh_window()

        elif "::family" in event:
            font_family = create_font_popup(
                "Familia da Fonte", "Insira a Familia da fonte"
            )
            refresh_window()

        elif "::theme" in event:
            current_theme = popup_combo(
                sg.theme_list(), current_theme, "Tema Padrão", "Selecione um Tema"
            )
            refresh_window()

        elif event == "-CONTENT-":
            update_status_bar(values["-CONTENT-"])

        # Mostrar o evento e os valores
        print(event, "=>", values)

    # Encerra a janela
    window.close()
