"""Represent a quote model."""


class QuoteModel:
    """Manipulates the body of the quote and author."""

    def __init__(self, body="", author=""):
        """Initialize body and author."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Represent how a quote should look."""
        return f"{self.body} - {self.author}"
