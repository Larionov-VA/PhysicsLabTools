from PySide6.QtWidgets import QMainWindow
from code_files.std_capture import Capturing

def main_init(main_window: QMainWindow):
    main_window.ui.generate.clicked.connect(lambda: generate_awnser(main_window))

def generate_awnser(main_window):
    mw = main_window
    list_of_values = [mw.ui.value_1.text(), mw.ui.value_2.text(), mw.ui.value_3.text(), mw.ui.value_4.text(), mw.ui.value_5.text()]
    try:list_of_values = list(map(float, list_of_values))
    except ValueError:
        mw.ui.console.setText("Введённые значения не являются числами.")
    else:
        from run_PLtools import gen_answer
        with Capturing() as output:
            gen_answer(list_of_values)
        mw.ui.console.setText("\n".join(output))
