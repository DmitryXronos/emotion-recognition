import os

DataPath = os.path.normpath(f"{os.getcwd()}{os.sep}{os.pardir}{os.sep}Data")

LabelsPath = os.path.normpath(f"{os.getcwd()}{os.sep}{os.pardir}{os.sep}Results{os.sep}Labels.csv")

FeaturesPath = os.path.normpath(f"{os.getcwd()}{os.sep}{os.pardir}{os.sep}Results{os.sep}Features.csv")


def extract_label_from_filename(file_name):
    """
    Извлекает метки эмоций из файла
    """
    labels = {
        "N": 0, "W": 1, "L": 2,
        "E": 3, "A": 4, "F": 5,
        "T": 6
    }
    if file_name[5] in labels.keys():
        return labels[file_name[5]]
    else:
        raise Exception("Неверное имя файла. Метка не может быть извлечена из полученного имени файла!")


def get_emotion_name_by_label(label):
    """
    Возвращает название эмоции по её метке
    """
    emotions = {
        0: "Нейтральность", 1: "Гнев", 2: "Скука",
        3: "Отвращение", 4: "Тревога", 5: "Счастье", 6: "Тоска"
    }
    if label in emotions.keys():
        return emotions[label]
    else:
        raise Exception("Неверная метка. Название эмоции не может быть извлечено из полученной метки!")
