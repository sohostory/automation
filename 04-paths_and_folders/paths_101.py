from pathlib import Path

p = Path('.')

print(p, ' is the current working directory')

home = Path.home()

print('The home directory is ', home)

doc_path = home / 'documents'

print(doc_path)

file_path = doc_path / 'my_file.txt'

print(file_path)

with open(file_path, 'r') as file:
    print(file.read())