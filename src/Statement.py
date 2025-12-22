"""
Definition for base credit card statement class
"""
from abc import ABC
from pathlib import Path

class Statement(ABC):
    def __init__(self, path: Path) -> None:
        """
        Base class for all credit card statement types.

        :param path: Path to credit card statement
        :type path: Path
        """
        self.path: Path = path
        """Path to credit card statement"""
