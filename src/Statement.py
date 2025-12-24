"""
Definition for base credit card statement class
"""
from abc import ABC
import csv
from pathlib import Path

class Statement(ABC):
    def __init__(self, path: Path) -> None:
        """
        Base class for all credit card statement types.

        :param path: Path to credit card statement
        :type path: Path
        """
        self.data: list[dict[str, str]]
        """Parsed .csv data"""
        with open(path, mode='r') as f:
            csv_reader = csv.DictReader(f)

            for row in csv_reader:
                self.data.append(row)
