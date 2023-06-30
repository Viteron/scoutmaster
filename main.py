import os


def get_path():
    "Функция получения адресса исполняемого файла"
    return os.getcwd()


def take_list_dirict():
    "Функция получения списка папок"
    return os.listdir()


def chenge_path_in_scout():
    "Функция изменения пути к видео в скаутах"
    pass


if __name__ == "__main__":
    #print(get_path())
    take_list_dirict()
    input("все готово!")
