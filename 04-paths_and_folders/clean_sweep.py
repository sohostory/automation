import shutil
from pathlib import Path

while True:
    directory = input("Please enter the path to directory: ")
    path = Path(directory).expanduser()

    if path.exists():
        break

    print('Invalid path. Please enter the valid path.')

closet = path / 'closet'
closet.mkdir(exist_ok=True)

text_files = closet / 'text_files'
csv_files = closet / 'csv_files'
folders = closet / 'folders'

text_files.mkdir(exist_ok=True)
csv_files.mkdir(exist_ok=True)
folders.mkdir(exist_ok=True)

for item in path.iterdir():
    if 'temp' in item.name.lower():
        if item.is_file():
            item.unlink(missing_ok=True)
        else:
            shutil.rmtree(item)
    elif item.name == 'closet':
        continue
    elif item.is_file() and item.suffix == '.txt':
        shutil.move(item, text_files / item.name)
    elif item.is_file() and item.suffix == '.csv':
        shutil.move(item, csv_files / item.name)
    elif item.is_dir():
        shutil.move(item, folders/item.name)
    else:
        shutil.move(item, closet/item.name)

print('Folder cleanup complete!')
