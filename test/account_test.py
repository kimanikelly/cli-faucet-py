import pytest

from app.account_model import *
from src.token_erc20 import Token
from src.deploy import *
from src.local_addresses import *

mint_amount = 100
fund_amount = 100


@pytest.fixture
def token():

    addresses["token_local_address"] = deploy_token().address

    return Token(w3.eth.default_account, 1337, "http://localhost:8545")


def test_account_class(token):

    token.mint(mint_amount)

    token.set_fund_amount(fund_amount)

    tx = token.fund_account()

    receipt = w3.eth.get_transaction_receipt(tx)

    from_address = token.contract.events.Transfer(
    ).processReceipt(receipt)[0].args['from']

    assert(from_address == token.address)

    to_address = token.contract.events.Transfer(
    ).processReceipt(receipt)[0].args['to']

    assert(to_address == w3.eth.default_account)

    value = token.contract.events.Transfer(
    ).processReceipt(receipt)[0].args['value']

    assert(value == w3.toWei(mint_amount, 'ether'))

    user_account = Account(to_address, from_address, value)

    assert(user_account.fetch_account_address() == w3.eth.default_account)
    assert(user_account.fetch_contract_address() == token.address)
    assert(user_account.fetch_amount() == w3.toWei(mint_amount, 'ether'))
