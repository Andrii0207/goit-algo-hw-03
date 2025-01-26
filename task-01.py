from pathlib import Path
from colorama import Fore, Style
import shutil


def backup_data(initial_path, backup_path="dist", indent=0, prefix=""):

    data = Path(initial_path)

    if data.is_dir():
        print(" " * indent + prefix + Fore.BLUE +
              f"{data}/" + Style.RESET_ALL)
        children = sorted(
            data.iterdir(), key=lambda x: (x.is_file(), x.name))

        for index, child in enumerate(children):
            is_last = index == len(children) - 1
            new_prefix = "└── " if is_last else "├── "
            backup_data(child, backup_path, indent + 4, new_prefix)

    else:
        print(" " * indent + prefix + Fore.YELLOW +
              f"{data.name}" + Style.RESET_ALL)
        ext = data.suffix
        new_path = Path(backup_path) / ext
        new_path.mkdir(exist_ok=True, parents=True)
        shutil.copyfile(data, new_path / data.name)


if __name__ == "__main__":

    backup_data("my_data", "backup")
