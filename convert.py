from PyQt5 import uic
import os

# Пути к файлам
ui_file_path = "D:/SpookyPlayer/newdesign.ui"
py_file_path = "D:/SpookyPlayer/newdesign.py"

# Убедитесь, что директория для .py файла существует
os.makedirs(os.path.dirname(py_file_path), exist_ok=True)

# Конвертация .ui в .py
with open(py_file_path, 'w', encoding='utf-8') as py_file:
    uic.compileUi(ui_file_path, py_file)

print(f"Файл {py_file_path} успешно создан.")
