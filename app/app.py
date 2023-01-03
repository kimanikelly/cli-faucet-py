import click
from account_model import Account
from src.token_erc20 import Token

from web3 import Web3

w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))

token = Token(w3.eth.default_account, 1337, "http://localhost:8545")


@click.group()
def cli():
    pass


@cli.command()
def fund_amount():
    print("Testing")


if __name__ == '__main__':
    cli()
