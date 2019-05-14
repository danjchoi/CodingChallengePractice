# [-Imports:Python-]
import sys


# [-Public-]
def main():
    """Main function."""
    def read_lines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = read_lines()

    # This works fine with file shell redirection due to the EoF
    # This does not work if someone just runs with stdin. It will wait for input forever?
    for line in lines:
        print(line.title())


if __name__ == "__main__":
    main()
