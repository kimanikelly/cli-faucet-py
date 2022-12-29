class Account:

    def __init__(self, account_address: str, contract_address: str, amount: int):

        self.account_address = account_address
        self.contract_address = contract_address
        self.amount = amount

    def fetch_account_address(self):
        return self.account_address

    def fetch_contract_address(self):
        return self.contract_address

    def fetch_amount(self):
        return self.amount
