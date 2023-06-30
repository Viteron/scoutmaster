import os


def get_path ():
    "Функция получения адресса исполняемого файла"
    return os.getcwd()
def create_file_with_name():
    # Открыть файл для записи
    with open(test, 'w') as file:
        # Записать имя файла внутри файла
        file.write(file_name)

# Пример использования функции

if __name__ == "__main__":
    print(get_path())
    input("все готово!")
