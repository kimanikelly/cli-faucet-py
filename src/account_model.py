class Account:

    def __init__(self, account_address: str, contract_address: str, token_name: str, token_symbol: str, amount: int):

        self.account_address = account_address
        self.contract_address = contract_address
        self.token_name = token_name
        self.token_symbol = token_symbol
        self.amount = amount

    def fetch_account_address(self):
        return self.account_address

    def fetch_contract_address(self):
        return self.contract_address

    def fetch_token_name(self):
        return self.token_name

    def fetch_token_symbol(self):
        return self.token_symbol

    def fetch_amount(self):
        return self.amount
