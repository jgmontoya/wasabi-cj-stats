import requests
import json

BASE_URL = 'https://blockstream.info/api'


class Explorer(object):
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def fetch_tx(self, txid):
        return json.loads(requests.get(BASE_URL + f'/tx/{txid}').text)

    def get_inputs(self, tx):
        return tx['vin']

    def amounts_from_inputs(self, inputs):
        amounts = [0] * len(inputs)
        for index, _input in enumerate(inputs):
            amounts[index] += _input['prevout']['value']
        return amounts

    def amounts_from_txid(self, txid):
        tx = self.fetch_tx(txid)
        inputs = self.get_inputs(tx)
        return self.amounts_from_inputs(inputs)


if __name__ == '__main__':
    explorer = Explorer()
    txid = 'ad01fe8c42b415cfb9e70b75cc219685ad825eb9c4de6d27349b5e136398f443'
    print(explorer.amounts_from_txid(txid))
