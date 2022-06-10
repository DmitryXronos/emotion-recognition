import os

DataPath = os.path.normpath(f"{os.getcwd()}{os.sep}{os.pardir}{os.sep}Data")

LabelsPath = os.path.normpath(f"{os.getcwd()}{os.sep}{os.pardir}{os.sep}Results{os.sep}Labels.csv")

FeaturesPath = os.path.normpath(f"{os.getcwd()}{os.sep}{os.pardir}{os.sep}Results{os.sep}Features.csv")


def extract_label_from_filename(file_name):
    """
    Extract emotion labels from filename
    """
    labels = {
        'N': 0, 'W': 1, 'L': 2,
        'E': 3, 'A': 4, 'F': 5,
        'T': 6
    }
    if file_name[5] in labels.keys():
        return labels[file_name[5]]
    else:
        raise Exception('Invalid filename. Could not extract the label from the file name')
