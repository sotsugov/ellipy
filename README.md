# Ellipy

Ellipy is a command-line tool that retrieves balance and metadata information for a given Bitcoin address using the Blockchain.info API. It provides a simple way to fetch and store the address details in a CSV file.

## Features

- Retrieve the balance of a Bitcoin address in BTC
- Fetch additional metadata such as total received, total sent, and the number of transactions
- Save the address information to a CSV file
- Append address information to an existing CSV file

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/sotsugov/ellipy.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To retrieve the balance and metadata for a Bitcoin address, run the following command:
```
python main.py ADDRESS [-o OUTPUT] [-a]
```

- `ADDRESS`: The Bitcoin address to retrieve information for (required).
- `-o OUTPUT`, `--output OUTPUT`: The output CSV file path (optional).
- `-a`, `--append`: Append the address information to an existing CSV file (optional).

Examples:
```
python main.py bc1pt73kxwl3dehkrxn96an0rd90k9d9apv4rtff4hmts7mkp6wr83zq4r7eap
python main.py bc1pt73kxwl3dehkrxn96an0rd90k9d9apv4rtff4hmts7mkp6wr83zq4r7eap -o output.csv
python main.py bc1pt73kxwl3dehkrxn96an0rd90k9d9apv4rtff4hmts7mkp6wr83zq4r7eap -o output.csv -a
```

## Testing

To run the unit tests for Ellipy, execute the following command:
```
python -m unittest -v
```

The tests are located in the `tests` directory and use the `unittest` module.
