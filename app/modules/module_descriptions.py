import os

MODULES_DIR = "app/modules"

def get_description(module_number: int) -> str:
    file_path = os.path.join(MODULES_DIR, f"module_{module_number}.ру")
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    return "Модуль не найден ❌"
