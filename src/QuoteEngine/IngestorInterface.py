"""The base form of Ingestor."""
from abc import abstractclassmethod, ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


ingestibles = {
    "TEXT": ".txt",
    "CSV": ".csv",
    "PDF": ".pdf",
    "DOCX": ".docx"
}


class IngestorInterface(ABC):
    """A class that sees whether a file is ingestible.
    Parses depending on type of file.
    """

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check that file is ingestible."""
        return path in ingestibles.values()

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """To be overwritten with concerned filetypes."""
        pass
