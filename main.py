import argparse
from src.ellipy import get_address_info
from src.utils import write_to_csv


def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(
        description="Retrieve Bitcoin address balance and metadata"
    )
    parser.add_argument("address", help="Bitcoin address to retrieve information for")
    parser.add_argument("-o", "--output", help="Output CSV file path")
    parser.add_argument(
        "-a", "--append", action="store_true", help="Append to existing CSV file"
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Get the address info
    address_info = get_address_info(args.address)

    if address_info:
        # Write the address info to a CSV file
        filename = args.output if args.output else f"{args.address}.csv"
        write_to_csv(address_info, filename, args.append)
        print(f"Address info saved to {filename}")


if __name__ == "__main__":
    main()
