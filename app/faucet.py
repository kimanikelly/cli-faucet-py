import click
import os
import dotenv
from web3 import Web3
from src.token_erc20 import Token

dotenv.load_dotenv()


assert os.getenv(
    "WALLET_ADDRESS") is not None, "You must set WALLET_ADDRESS environment variable"
assert os.getenv("WALLET_ADDRESS").startswith(
    "0x"), "Wallet address must start with 0x hex prefix"

assert os.getenv(
    "PRIVATE_KEY") is not None, "You must set PRIVATE_KEY environment variable"
assert os.getenv("PRIVATE_KEY").startswith(
    "0x"), "Private key must start with 0x hex prefix"

assert os.getenv(
    "GOERLI_PROVIDER") is not None, "You must set GOERLI_PROVIDER environment variable"

w3 = Web3(Web3.HTTPProvider(os.getenv("GOERLI_PROVIDER")))

token = Token(os.getenv("WALLET_ADDRESS"), 5,
              os.getenv("GOERLI_PROVIDER"))

nonce = w3.eth.get_transaction_count(os.getenv("WALLET_ADDRESS"))


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

    tx = token.fund_account().build_transaction({
        'chainId': 5,
        'from': os.getenv("WALLET_ADDRESS"),
        'nonce': nonce
    })

    sign_tx = w3.eth.account.sign_transaction(
        tx, private_key=os.getenv("PRIVATE_KEY"))

    tx_hash = w3.eth.send_raw_transaction(sign_tx.rawTransaction)

    print(tx_hash)


if __name__ == '__main__':
    cli()
