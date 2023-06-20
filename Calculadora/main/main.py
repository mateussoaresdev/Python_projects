# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

from view import create_main_window


def calculate(operation, total, actual):
    if operation == "+":
        return total + actual
    elif operation == "-":
        return total - actual
    elif operation == "*":
        return total * actual
    else:
        if actual == 0:
            sg.Popup("Não pode dividir por 0")
            return total
        else:
            return total / actual


# Verifica se estamos executando esse arquivo como sendo o principal
if __name__ == "__main__":

    # Definindo a janela inicial
    window = create_main_window(theme="DarkGrey9")

    operators = ["+", "-", "*", "/"]

    total = 0
    operation = ""
    resulting = False
    calculating = False

    # [Numero]  [OP]   [Numero]
    #
    #    10
    #    [10]      +   => Início do Calculo
    #    10      +        20
    #    10     [+]       20     [=]    => Calcular
    #    30     [+]
    #    30     [+]   10
    #    30     [+]   10    [=] 40

    # total = 10
    # operador = +
    # atual = 20
    # resulto = 10 + 20

    # Loop da Leitura da janela
    while True:
        # Coletar Eventos e Valores atuais
        event, values = window.read()

        # Cancelar o loop ao fechar a janela
        if event == sg.WIN_CLOSED:
            break

        # Mostrar o evento e os valores
        # print(event, "=>", values)

        if event in operators:
            if not calculating:
                calculating = True
                total = float(values["-VALUE-"])
            else:
                actual = float(values["-VALUE-"])
                total = calculate(operation, total, actual)
                window["-VALUE-"].update(total)

            operation = event
            window["-VALUE-"].update("0")
            resulting = False

        elif event == "=":
            if calculating:
                resulting = True
                actual = float(values["-VALUE-"])
                total = calculate(operation, total, actual)
                window["-VALUE-"].update(total)

        elif event == "<<":
            if not resulting:
                current_value = values["-VALUE-"]
                new_value = current_value[:-1]

                if new_value == "":
                    new_value = "0"

                window["-VALUE-"].update(new_value)

        elif event == "C":
            window["-VALUE-"].update("0")
            total = 0
            operation = ""
            resulting = False
            calculating = False

        else:
            if not resulting:
                current_value = values["-VALUE-"]

                if current_value == "0":
                    if event != ".":
                        current_value = ""

                if event == ".":
                    if "." in current_value:
                        continue

                window["-VALUE-"].update(current_value + event)

    # Encerra a janela
    window.close()
