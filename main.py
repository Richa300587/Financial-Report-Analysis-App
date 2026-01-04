from pathlib import Path
from unstructured.partition.pdf import partition_pdf
from src.logger import configure_logging, get_logger
from exceptions import TableIntegrityError, RAGException
from src.constants import *
# Configure logging ONCE
configure_logging()

logger = get_logger(__name__)
print("Files can be found in venv")