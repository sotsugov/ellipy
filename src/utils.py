import csv


def write_to_csv(data, filename, append=False):
    fieldnames = [
        "address",
        "balance_btc",
        "total_received_btc",
        "total_sent_btc",
        "num_transactions",
    ]

    mode = "a" if append else "w"
    with open(filename, mode=mode, newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not append:
            writer.writeheader()

        writer.writerow(data)
