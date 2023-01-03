import click
import os
import dotenv
from web3 import Web3
from src.token_erc20 import Token

dotenv.load_dotenv()


user_address = os.getenv("USER_ADDRESS")

goerli_provider = os.getenv("GOERLI_PROVIDER")

token = Token(user_address, 5, goerli_provider)

w3 = Web3(Web3.HTTPProvider(goerli_provider))


@click.group()
def cli():
    pass


@cli.command(help="The amount of Test Tokens transferred to a wallet")
def fund_amount():

    click.echo(
        f"The fund amount is: {w3.fromWei(token.fetch_fund_amount(), 'ether')} TT")


@cli.command(help="View the amount of Test Tokens Token.sol holds")
def contract_balance():

    click.echo(
        f"The contract balance is: {w3.fromWei(token.fetch_balance_of(token.address),'ether')} TT")


if __name__ == '__main__':
    cli()
