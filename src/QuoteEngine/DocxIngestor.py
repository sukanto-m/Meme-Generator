"""Ingestor for docx files."""

import docx
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class DocxIngestor(IngestorInterface):
    """Ingest info from docx files."""

    @classmethod
    def parse(cls, path):
        """Parse from docx file."""
        quotes = []
        doc = docx.Document(path)
        for para in doc.paragraphs:
            if para.text != "":
                p = para.text.split('-')
                new_quote = QuoteModel(p[0].strip(), p[1].strip())
                quotes.append(new_quote)
        return quotes
