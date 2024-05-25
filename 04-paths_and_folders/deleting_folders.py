from pathlib import Path
import shutil

src = Path.home() / 'documents' / 'python_automation' / 'doomed_folder'

if src.exists():
    src.rmdir()

src2 = Path.home() / 'documents' / 'python_automation' / 'fun_w_folders'

if src2.exists():
    shutil.rmtree(src2)