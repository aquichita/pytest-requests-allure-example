import logging
from pathlib import Path

_logfile = Path(".").resolve() / Path("gofers.out")

logging.basicConfig(
    filename=_logfile,
    level=logging.DEBUG
)


logging.info(Path(".").resolve())
