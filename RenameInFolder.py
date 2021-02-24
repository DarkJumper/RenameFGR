import os
import time
import yaml


def write_yaml(path, fgr_list):
    dict_file = [{"FGR": fgr_list}]
    with open(f'{path}\\FGR.yaml', 'w') as file:
        documents = yaml.dump(dict_file, file, allow_unicode=True)


def read_yaml(path):
    with open(f'{path}\\FGR.yaml', 'r') as file:
        documents = yaml.load(file)
        return documents


def write_information(path, information):
    with open(f'{path}\\.info.txt', 'w') as file:
        file.write(information)


class RenameInFolder:

    def __init__(self) -> None:
        self.start_dir = set(os.listdir())
        self.current_dir = os.path.abspath("")

    def run(self) -> None:
        try:
            temp = read_yaml(self.current_dir)
            while len(temp[0]["FGR"]) != 0:
                time.sleep(3)
                print("Zeit abgelaufen")
                temp = read_yaml(self.current_dir)
                current_folder = set(os.listdir())
                if self.start_dir != current_folder:
                    for file in current_folder:
                        if file not in self.start_dir:
                            self.rename(file)
                    self.start_dir = set(os.listdir())
        except:
            write_information(self.current_dir, "Exception im Run!")
            return None

    def rename(self, file) -> None:
        old_file_list = file.split(".")
        temp = read_yaml(os.path.abspath("."))
        old_file = f'{self.current_dir}\\{file}'
        new_filename = temp[0]["FGR"].pop(0)
        new_file = f'{self.current_dir}\\{new_filename}.{old_file_list[-1]}'
        try:
            os.rename(old_file, new_file)
            write_yaml(self.current_dir, temp[0]["FGR"])
        except FileNotFoundError:
            write_information(self.current_dir, "File not found Rename!")
            return None


if __name__ == '__main__':
    RenameInFolder().run()
