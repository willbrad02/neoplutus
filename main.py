"""
Generate a dashboard showing
"""
from argparse import ArgumentParser, Namespace
from pathlib import Path

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

def _validate_user_args(apple: Path, chase: Path, amex: Path) -> None:

    # Check Apple path
    if not apple.is_file():
        raise # TODO: Implement error (see https://www.geeksforgeeks.org/python/how-to-handle-invalid-arguments-with-argparse-in-python/)


if __name__ == "__main__":
    # Grab command line arguments
    user_args: Namespace = _get_user_args()

    # Convert args to Path objects
    apple_path: Path = Path(user_args.apple)
    chase_path: Path = Path(user_args.chase)
    amex_path:  Path = Path(user_args.amex)

    # Validate args
    try:
        _validate_user_args(apple_path, chase_path, amex_path)

    # TODO: Specify error type?
    except Exception as e:
        print(e)
