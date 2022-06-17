from shutil import rmtree
from os import mkdir, path

# Delete directory
def delete_dir(dir: str) -> None:
    if path.exists(dir): rmtree(dir)

# Create temp folder
def create_temp() -> None:
    if path.exists('temp'): rmtree('temp')

    mkdir('temp')
    mkdir('temp/pictures')
    mkdir('temp/videos')
    mkdir('temp/audios')