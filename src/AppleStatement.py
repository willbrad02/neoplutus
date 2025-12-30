"""
Definition for Apple credit card statement class.
"""
from pathlib import Path

from Statement import Statement
from string_resources import _AppleStatement # type: ignore

class AppleStatement(Statement):
    """Apple credit card statement."""

    transact_date: str = _AppleStatement.TRANSACTION_DATE
    """Transaction date"""

    clear_date:    str = _AppleStatement.CLEARING_DATE
    """Transaction clearing date"""

    description:   str = _AppleStatement.DESCRIPTION
    """Transaction description"""

    merchant:      str = _AppleStatement.MERCHANT
    """Transaction merchant"""

    category:      str = _AppleStatement.CATEGORY
    """Transaction category"""

    type:          str = _AppleStatement.TYPE
    """Transaction type"""

    amount:        str = _AppleStatement.AMOUNT
    """Transaction amount"""

    def __init__(self, path: Path) -> None:
        """
        Apple credit card  constructor.

        :param path: Path to credit card statement
        :type path: Path
        """
        super().__init__(path)

        # Calculate totals
        for row in self.data:
            if row[self.type] == _AppleStatement.PURCHASE: # Total transaction amount
                self.total += float(row[self.type])
            elif row[self.type] == _AppleStatement.PAYMENT: # Total payments made
                self.tot_payment += float(row[self.type])
