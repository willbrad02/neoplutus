"""
Definition for base credit card statement class.
"""
from abc import ABC
import csv
from pathlib import Path

class Statement(ABC):
    """Base class for all credit card statement types."""

    def __init__(self, path: Path) -> None:
        """
        Base class constructor.

        :param path: Path to credit card statement
        :type path: Path
        """
        self.data: list[dict[str, str]] = []
        """Rows of .csv data"""

        self.total: float = 0.0
        """Total transaction amount"""

        self.tot_payment: float = 0.0
        """Total amount of payments made"""

        # Read and parse .csv
        with open(path, mode='r') as f:
            csv_reader = csv.DictReader(f)

            for row in csv_reader:
                self.data.append(row)
