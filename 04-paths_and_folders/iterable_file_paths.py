from pathlib import Path
from datetime import datetime

path = Path.home() / 'code' / 'automation' / 'automation' / '03-working_with_files' / 'plaintext-files'

for item in path.iterdir():
    if item.is_file() and item.suffix == '.txt':
        print(item.stem, 'is a text file.')
        stats = item.stat()

        print("Size: ", stats.st_size)
        print('Last Modified: ', datetime.fromtimestamp(stats.st_mtime))

    if item.is_dir():
        print(item.name, 'is a directory.')

    if 'read' in item.name.lower():
        print(item.name, "contains the word 'read'")