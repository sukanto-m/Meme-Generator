"""Ingestor for parsing csv files."""
import pandas as pd
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class CSVIngestor(IngestorInterface):
    """Ingest info from csv files."""

    @classmethod
    def parse(cls, path):
        """Parse csv file."""
        csv = pd.read_csv(path, header=0)
        quotes = []

        for index, row in csv.iterrows():
            new_quote = QuoteModel(row['body'].strip(), row['author'].strip())
            quotes.append(new_quote)
        return quotes
