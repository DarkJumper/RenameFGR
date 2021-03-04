import pyautogui
import keyboard
import time
import yaml
import os


def read_yaml(path):
    with open(f'{path}\\FGR.yaml', 'r') as file:
        documents = yaml.load(file)
        return documents


class TakeScreenShot:
    status = 1

    def __init__(self) -> None:
        temp = read_yaml(os.path.abspath(""))
        self.yaml_data = temp[0]["FGR"]

    def screenshot(self, name):
        im1 = pyautogui.screenshot()
        im2 = pyautogui.screenshot(f'{name}.jpg')

    def run(self):
        for new_filename in self.yaml_data:
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'f6')
            pyautogui.write(new_filename)
            pyautogui.hotkey('enter')
            time.sleep(2)
            new_filename.replace('/', '_')
            new_filename.replace('ä', 'ae')
            new_filename.replace('ö', 'oe')
            new_filename.replace('ü', 'ue')
            new_filename.replace('Ä', 'Ae')
            new_filename.replace('Ö', 'Oe')
            new_filename.replace('Ü', 'Ue')
            self.screenshot(new_filename)
        self.status = 0


def main():
    list_dir = os.listdir()
    temp = read_yaml(os.path.abspath(""))
    end_len = len(temp[0]["FGR"]) + len(list_dir)
    while len(list_dir) != end_len:
        time.sleep(1)
        shot = TakeScreenShot()
        keyboard.add_hotkey('f11', lambda: shot.run())
        list_dir = os.listdir()


if __name__ == "__main__":
    main()
