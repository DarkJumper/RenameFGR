import os
import yaml
import tkinter
from tkinter import filedialog


def writeYaml(path, fgr_list):
    dict_file = [{"FGR": fgr_list}]
    with open(f'{path}\\FGR.yaml', 'w') as file:
        documents = yaml.dump(dict_file, file, allow_unicode=True)


def create_yaml_data():
    root = tkinter.Tk()
    csv_dir = filedialog.askopenfilename(filetypes=(("Csv files", "*.csv;*.csv"), ("All files", "*.*")))
    fgr_list = list()
    try:
        with open(csv_dir, 'r', newline='', encoding='utf-16') as file:
            for row in file:
                splitted_row = row.strip().split(";")
                if '[PBV:OBJPATH]' in row and "FGRBLT" in row and not "Pool" in row:
                    new_name = splitted_row[-1].replace("/", "_")
                    fgr_list.append(new_name)
            fgr_list.sort()
            writeYaml(os.path.abspath("."), fgr_list)
            root.destroy()
    except FileNotFoundError:
        print("Datei konnte nicht gefunden werden!")


if __name__ == '__main__':
    create_yaml_data()