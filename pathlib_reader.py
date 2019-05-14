# [-Imports:Python-]
import pathlib
import sys


# [-Public-]
def main():
    """The main function."""
    if len(sys.argv) < 2:
        raise RuntimeError("No input filename supplied")
    input_file_name = sys.argv[1]
    input_path = pathlib.Path(input_file_name)
    try:
        print(input_path.read_text())
    except FileNotFoundError as error:
        raise RuntimeError(f"Invalid filename '{input_file_name}'") from error

if __name__ == "__main__":
    main()
