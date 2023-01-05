import click
import os
import dotenv
from web3 import Web3
from src.token_erc20 import Token

dotenv.load_dotenv()

user_address = os.getenv("USER_ADDRESS")

goerli_provider = os.getenv("GOERLI_PROVIDER")

goerli_chain_id = 5

w3 = Web3(Web3.HTTPProvider(goerli_provider))

token = Token(user_address, goerli_chain_id, goerli_provider)


@click.group()
def cli():
    pass


@cli.command(help="View the amount of TT transferred to a wallet")
def fund_amount():

    click.echo(
        f"The fund amount is: {click.style(w3.fromWei(token.fetch_fund_amount(), 'ether'),fg='magenta')} TT")


@cli.command(help="View the amount of TT Token.sol holds in the contract")
def contract_balance():

    click.echo(
        f"The contract balance is: {click.style(w3.fromWei(token.fetch_balance_of(token.address),'ether'),fg='magenta')} TT")


@cli.command(help="View the amount of TT an address holds in their wallet")
@click.argument("address")
def balance_of(address):

    click.echo(
        f"The TT balance of {click.style(address,fg='magenta')} is: {click.style(w3.fromWei(token.fetch_balance_of(address),'ether'),fg='magenta')} TT")


@cli.command("goerli-balance-of", help="View the amount of GoerliETH an address holds in their wallet")
@click.argument("address")
def eth_balance_of(address):

    click.echo(
        f"The GoerliETH balance of {click.style(address,fg='magenta')} is: {click.style(w3.fromWei(w3.eth.get_balance(address),'ether'),fg='magenta')} GoerliETH")


@cli.command(help="Transfers the fund amount from Token.sol to the connected wallet")
def fund_account():
    token.fund_account()


if __name__ == '__main__':
    cli()
