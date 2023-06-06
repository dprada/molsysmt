import os
from pathlib import Path

data_dir = Path('../../data/.')

files_to_be_purged = [
        'msmpk/divaline.msmpk',
        ]

for filename in files_to_be_purged:
    filepath = Path(data_dir, filename)
    if os.path.isfile(filepath):
        os.remove(filepath)

print('DONE')
