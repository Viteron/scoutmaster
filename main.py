import os


def get_path ():
    "Функция получения адресса исполняемого файла"
    return os.getcwd()


if __name__ == "__main__":
    print(get_path())
    input("все готово!")
