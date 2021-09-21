"""Determine which ingestor to use."""
import os
from .IngestorInterface import IngestorInterface
from .TextIngestor import TextIngestor
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor


ingestibles = {
    "TEXT": ".txt",
    "CSV": ".csv",
    "PDF": ".pdf",
    "DOCX": ".docx"
}


class Ingestor(IngestorInterface):
    """Determine ingestor strategy."""

    @classmethod
    def parse(cls, path):
        """Get the file, determine ingestor strategy."""
        filename, file_extension = os.path.splitext(path)
        if not Ingestor.can_ingest(file_extension):
            raise ValueError('Unsupported file extension: ', file_extension)
        if file_extension == ingestibles.get("TEXT"):
            return TextIngestor.parse(path)
        if file_extension == ingestibles.get("CSV"):
            return CSVIngestor.parse(path)
        if file_extension == ingestibles.get("DOCX"):
            return DocxIngestor.parse(path)
        if file_extension == ingestibles.get("PDF"):
            return PDFIngestor.parse(path)
