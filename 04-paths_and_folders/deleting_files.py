from pathlib import Path


src = Path.home() / 'documents' / 'python_automation' / 'moving_n_renaming' / 'my_123rd_folder' / 'sad_jokes.txt'

src.unlink(missing_ok=True)