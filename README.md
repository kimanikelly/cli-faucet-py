# cli-faucet-py

[![Python application](https://github.com/kimanikelly/cli-faucet-py/actions/workflows/python-app.yml/badge.svg)](https://github.com/kimanikelly/cli-faucet-py/actions/workflows/python-app.yml)

## Source Code Installation

Clone the repo

```
https://github.com/kimanikelly/cli-faucet-py.git
```

Install the dependencies

```
pip install -r ./requirements.txt
```

## Token.sol (TT) Information

Token.sol Goerli Etherscan link

```
https://goerli.etherscan.io/address/0xc8d16da2b9b9a30c0cadcf72b91a4a9f1739f39e
```

Token.sol contract address

```
0xC8D16Da2B9b9a30c0CADcF72B91a4A9f1739f39e
```

Token.sol source Code

```
https://github.com/kimanikelly/contracts/blob/main/contracts/Token.sol
```

## Setup Environment Variables

Create a .env file

```
touch .env
```

After creating the .env file set the environment variables by using [.env.example](.env.example) as a template

## CLI Commands

- [fund-amount](docs/fundAmount.md)
- [contract-balance](docs/contractBalance.md)
- [balance-of](docs/balanceOf.md)
- [goerli-balance-of](docs/goerliBalanceOf.md)
- [fund-account](docs/fundAccount.md)
