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

    token.fund_account()

    user_account = Account(w3.eth.default_account, token.address, mint_amount)

    assert(user_account.fetch_account_address() == w3.eth.default_account)
    assert(user_account.fetch_contract_address() == token.address)
    assert(user_account.fetch_amount() == mint_amount)
