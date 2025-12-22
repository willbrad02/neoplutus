"""
Definition for Apple credit card statement class
"""
from pathlib import Path
from Statement import Statement

class AppleStatement(Statement):
    def __init__(self, path: Path) -> None:
        """
        Apple credit card statement

        :param path: Path to credit card statement
        :type path: Path
        """
        super().__init__(path)