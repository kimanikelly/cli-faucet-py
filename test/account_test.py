from src.account_model import Account


def test_account():
    testing = Account("xyz")

    assert(testing.account_address == "xyz")
