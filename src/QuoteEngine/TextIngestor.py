"""Ingest text files."""

import pandas as pd
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class TextIngestor(IngestorInterface):
    """Ingests from text."""

    @classmethod
    def parse(cls, path):
        """Parse text files."""
        quotes = []
        file = open(path, 'r', encoding='utf-8-sig')
        lines = file.readlines()
        file.close()
        for quote in lines:
            p = quote.rstrip("\n").split(" - ")
            q = QuoteModel(p[0].strip(), p[1].strip())
            quotes.append(q)
        return quotes
