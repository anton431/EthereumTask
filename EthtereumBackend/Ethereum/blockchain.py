import json
import os
from dotenv import load_dotenv, find_dotenv
from web3 import Web3, HTTPProvider
from django.core.management.utils import get_random_string
import string


load_dotenv(find_dotenv())
infura_url = f'https://goerli.infura.io/v3/{os.getenv("API_Key")}'
w3 = Web3(HTTPProvider(infura_url))

def get_contract(owner):
    owner = Web3.toChecksumAddress(owner)
    with open("Contract_ABI.json", "r") as read_file:
        NFT_ABI = json.load(read_file)
    nft_contract = w3.eth.contract(address=owner, abi=NFT_ABI)
    return nft_contract

def random_srting():
    # Метод создания хеша токена (не уникального!)
    chars = string.ascii_lowercase + string.digits
    return get_random_string(20, chars)


def mint(owner_metamask, media_url, unique_hash):
    nft_contract = get_contract(owner_metamask)
    nonce = w3.eth.get_transaction_count(owner_metamask)
    print(nonce)
    tx = nft_contract.functions.mint(
        owner=owner_metamask, uniqueHash=unique_hash, mediaURL=media_url
    ).buildTransaction({
        'chainId': w3.eth.chain_id,
        'gas': 220000,
        'gasPrice': w3.eth.gas_price,
        'nonce': nonce,
    })
    signed_tx = w3.eth.account.sign_transaction(tx, os.getenv("PRIVATE_KEY"))
    tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash.hex()

def supply():
    nft_contract = get_contract(os.getenv('owner'))
    return nft_contract.functions.totalSupply().call()
