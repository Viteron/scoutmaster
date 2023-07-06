import glob
import os
import shutil



def get_path():
    "Функция получения адресса исполняемого файла"
    return os.getcwd()


def take_list_dirict():
    "Функция получения списка папок"
    return os.listdir()


def find_name_video(path_folder):
    "Функция вывода имени видео формата .avi или .mp4"
    avi_files = glob.glob(path_folder + '/*.avi')
    mp4_files = glob.glob(path_folder + '/*.mp4')
    if len(avi_files) == 1:
        avi_name = os.path.split(avi_files[0])
        return avi_name[1]
    else:
        if len(mp4_files) == 1:
            mp4_name = os.path.split(mp4_files[0])
            return mp4_name[1]
        else:
            print("Проверьте наличие видео в папке: " + path_folder)
            return "non video"


def find_text_in_file(file_name, search_text):
    "Функция для вывода индекса с нужным текстом"
    with open(file_name, 'r') as file:
        lines = file.readlines()
    file.close()
    for index, line in enumerate(lines):
        if search_text in line:
            return index
    return -1  # Если текст не найден


def replace_line_in_file(file_name, index, new_line):
    "Функция для замены нужной строки в файле"
    with open(file_name, 'r') as file:
        lines = file.readlines()
    file.close()
    if index < 0 or index >= len(lines):
        print("Недопустимый индекс строки.")
        return
    lines[index] = new_line
    with open(file_name, 'w') as file:
        file.writelines(lines)
        file.close()


def chenge_path_in_scout():
    "Функция изменения пути к видео в скаутах"
    my_list = take_list_dirict()
    adress = get_path()+"\\"
    new_directory = "00_all_scouts"
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    for name_folder in my_list:
        full_adress = adress + name_folder
        dvw_files = glob.glob(full_adress + '/*.dvw')
        name_video = find_name_video(full_adress)
        adress_video = full_adress+"\\" + name_video
        for file_path in dvw_files:
            index = find_text_in_file(file_path, "Camera0=")
            modified_adress_video = adress_video.replace("\\\\", "\\")
            final_adress_video = "Camera0=" + modified_adress_video + "\n"
            replace_line_in_file(file_path, index, final_adress_video)
            shutil.copy(file_path, adress+new_directory)

            
def get_new_name_withs_scout(path_folder):
    "Получение названия папки из скаута"
    dvw_files = glob.glob(path_folder + '/*.dvw')
    if len(dvw_files) == 1:
        dvw_name = os.path.split(dvw_files[0])
        return dvw_name[1][1:-4]
    else:
        print("в папке " + path_folder + " нет скаута")
        return False

def rename_folder ():
    "переименовывает папку как скаут"
    base_path = os.getcwd() #путь где находиться программа
    list_dir = os.listdir()
    for folder in list_dir:
        old_folder_path = base_path + '\\' + folder
        new_name = get_new_name_withs_scout(old_folder_path)
        if not new_name:
            continue
        full_path_new_name = base_path + '\\' + new_name
        os.rename(old_folder_path, full_path_new_name)



if __name__ == "__main__":
    chenge_path_in_scout()
    rename_folder()

