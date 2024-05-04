import requests


def get_address_info(address):
    try:
        # Make a GET request to the Blockchain.info API
        url = f"https://blockchain.info/q/addressbalance/{address}"
        response = requests.get(url)

        if response.status_code == 200:
            # Extract the balance from the response
            balance = int(response.text)

            # Convert the balance from satoshis to bitcoins
            balance_btc = balance / 100000000

            # Make another request to get additional metadata
            url = f"https://blockchain.info/rawaddr/{address}"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                total_received = data["total_received"] / 100000000
                total_sent = data["total_sent"] / 100000000
                num_transactions = data["n_tx"]

                # Create a dictionary with the address info
                address_info = {
                    "address": address,
                    "balance_btc": balance_btc,
                    "total_received_btc": total_received,
                    "total_sent_btc": total_sent,
                    "num_transactions": num_transactions,
                }

                return address_info
            else:
                raise ValueError(
                    f"Failed to retrieve additional metadata for address: {address}"
                )
        else:
            raise ValueError(f"Failed to retrieve balance for address: {address}")
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(
            f"An error occurred while making the request: {e}"
        )
