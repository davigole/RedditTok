import os
from master.console import create_log
from master.background import download_sample

if __name__ == '__main__':
    log = create_log()
    path = 'assets/background.mp4'

    log.info('Downloading sample background video at {}. This may take a while'.format(path))
    download_sample(path)