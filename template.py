import logging
import os

from pathlib import Path

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    'artifacts/raw/data',
    'src/__init__.py',
    'src/utils/__init__.py',
    'src/utils/logger.py',
    'src/utils/custom_exception.py',
    'src/chain/__init__.py',
    'src/chain/itinerary_chain.py',
    'src/core/__init__.py',
    'src/core/planner.py',
    'pipeline/__init__.py',
    'src/config/__init__.py',
    'src/config/config.py',
    '.env',
    'app.py',
    '.gitignore',
    'k8s-deployment.yaml',
    'filebeat.yaml',
    'logstash.yaml',
    'elasticsearch.yaml',
    'kibana.yaml'
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory: {filedir} for the file {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f'Creating empty file: {filepath}')

    else:
        logging.info(f'{filename} already exists')
