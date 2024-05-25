from pathlib import Path

# p = r'~/Code'
p = input('Please enter the target folder: ')

path = Path(p).expanduser()

if path.exists():
    print(path)