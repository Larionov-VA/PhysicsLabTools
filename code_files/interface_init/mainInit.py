from PySide6.QtWidgets import QMainWindow
from code_files.std_capture import Capturing
from run_PLtools import *

# инициализация кнопок основного окна
def main_init(main_window: QMainWindow):
    main_window.current_amount = 10
    main_window.ui.generate.clicked.connect(lambda: generate_awnser(main_window))
    main_window.ui.change_amount_of_values.clicked.connect(lambda: change_values(main_window))
    main_window.ui.generate_docx.clicked.connect(lambda: generate_docx(main_window))


# выводит в сгенерированые значения в консоль окна
def generate_awnser(main_window):
    mw = main_window

    # проверка на случай ввода неверных значений
    try:list_of_values = list(map(float, get_values(mw)))
    except ValueError:
        mw.ui.console.setText("Введённые значения не являются числами.")
    else:
        # from run_PLtools import gen_answer
        with Capturing() as output:
            gen_answer(list_of_values, False)
        mw.ui.console.setText("\n".join(output))

def generate_docx(main_window):
    mw = main_window
    try:list_of_values = list(map(float, get_values(mw)))
    except ValueError:
        mw.ui.console.setText("Введённые значения не являются числами.")
    else:
        try: instrument_error = float(mw.ui.instrument_error.text())
        except ValueError:
            mw.ui.console.setText("Введённое значение погрешности не является числом.")
            return
        if has_numbers(mw.ui.symbol.text()) or mw.ui.symbol.text() == "":
            mw.ui.console.setText("Введённое значение символа имеет цифры или пусто.")
            return
        symbol = mw.ui.symbol.text()
        from make_docx import makeDocument
        with Capturing() as output:
            try: makeDocument(list_of_values, instrument_error, symbol)
            except ValueError as e: print(str(e))
        mw.ui.console.setText("\n".join(output))

def change_values(main_window):
    mw = main_window
    try: mw.current_amount = int(mw.ui.amount_of_values_to_change.text())
    except ValueError or AttributeError:
        pass
    else:
        mw.ui.amount_of_values_to_change.clear()
        mw.ui.values.setRowCount(mw.current_amount)

def get_values(main_window) -> list:
    returned_list = list()
    for i in range(main_window.current_amount):
        try: returned_list.append(main_window.ui.values.item(i, 0).text())
        except AttributeError: raise ValueError
    return returned_list

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)
