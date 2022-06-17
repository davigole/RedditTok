import logging
from rich.logging import RichHandler

# Create log object
def create_log(log_file: bool=False) -> logging.Logger:
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler()]
    )
    return logging.getLogger("rich")