"""
Generate a dashboard showing
"""
from argparse import ArgumentParser, Namespace
from pathlib import Path

from AppleStatement import AppleStatement
from Statement import Statement

ALLOWABLE_F_TYPES: list[str] = [".csv"]

def _get_user_args() -> Namespace:
    """
    Get and parse command line arguments.

    :return: Parsed command line arguments
    :rtype: Namespace
    """
    arg_parser: ArgumentParser = ArgumentParser(
        description="Collate inputted credit card statements into a single dashboard"
    )

    arg_parser.add_argument(
        "-a",
        "--apple",
        # metavar="APPLE CARD PATH",
        type=str,
        default="",
        help="Path to Apple credit card statement. Must be .csv"
    )

    arg_parser.add_argument(
        "-c",
        "--chase",
        # metavar="CHASE CARD PATH",
        type=str,
        default="",
        help="Path to Chase credit card statement. Must be .csv"
    )

    arg_parser.add_argument(
        "-e",
        "--amex",
        # metavar="AMEX CARD PATH",
        type=str,
        default="",
        help="Path to American Express credit card statement. Must be .csv"
    )

    return arg_parser.parse_args()

def _validate_user_args(args: dict[str, str]) -> None:
    """
    Validate command line arguments

    :param args: Object containing passed user arguments
    :type args: dict[str, str]
    """
    # Valid args must be a file and have the correct file extension
    # TODO: Implement error (see https://www.geeksforgeeks.org/python/how-to-handle-invalid-arguments-with-argparse-in-python/)
    for arg in args.values():
        if not Path(arg).is_file() or (Path(arg).suffix.lower() not in ALLOWABLE_F_TYPES):
            raise ValueError(f"Invalid path: {arg}")

def _parse_user_args(args: dict[str, str]) -> list[Statement]:
    """
    Parse command line arguments

    :param args: Object containing validated user arguments
    :type args: dict[str, str]
    :return: Description
    :rtype: list[Statement]
    """
    parsed_args: list[Statement] = []

    for company, path in args.items():
        # TODO: switch statement for each credit card company. Subclass Statement for each company
        # TODO: Better software structure than hardcoded company names in switch statement?
        cc_statement: Statement
        match company:
            case "apple":
                cc_statement = AppleStatement(Path(path))
            case _:
                cc_statement = Statement(Path(path))

        parsed_args.append(cc_statement)

    return parsed_args


if __name__ == "__main__":
    # Grab command line arguments and convert to dictionary
    user_args: Namespace = _get_user_args()
    args_dict: dict[str, str] = vars(user_args)

    # Validate args
    try:
        _validate_user_args(args_dict)

    # TODO: Specify error type?
    except Exception as e:
        print(e)

    # Parse args and convert to workable class
    parsed_args: list[Statement] = _parse_user_args(args_dict)
