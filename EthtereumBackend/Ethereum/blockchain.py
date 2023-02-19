import json
import os
from dotenv import load_dotenv, find_dotenv
from secrets import choice
from web3 import Web3, HTTPProvider
from django.core.management.utils import get_random_string
import string

load_dotenv(find_dotenv())


def random_srting():
    # Метод создания хеша токена (не уникального!)
    chars = string.ascii_lowercase + string.digits
    return get_random_string(20, chars)


def mint(owner, media_url, unique_hash):
    # Метод создания токена в блокчейне, возвращает хэш транзакции создания
    owner = Web3.toChecksumAddress(owner)
    infura_url = f'https://celo-mainnet.infura.io/v3/{os.getenv("API_Key")}'
    w3 = Web3(HTTPProvider(infura_url))
    with open(r"C:\Users\anton\python\Ethereum\EthtereumBackend\Ethereum\Contract_ABI.json", "r") as read_file:
        NFT_ABI = json.load(read_file)
    nft_contract = w3.eth.contract(address=owner, abi=NFT_ABI)
    nonce = w3.eth.get_transaction_count(owner)
    tx = nft_contract.functions.mint(
        owner=owner, uniqueHash=unique_hash, mediaURL=media_url
    ).buildTransaction({
        'chainId': w3.eth.chain_id,
        'gas': 20000,
        'gasPrice': w3.eth.gas_price,
        'nonce': nonce})
    # Так не смог получить для теста ETH в Metamask, tx_hash будет принимать значение tx['data'][392:486],
    # далее следует две строки кода, если бы были токены
    # signed_tx = w3.eth.account.sign_transaction(tx, os.getenv("PRIVATE_KEY"))
    # tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx['data'][392:486]


# def totalSupply():
#     return _allTokens.length

