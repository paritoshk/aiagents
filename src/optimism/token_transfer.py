import os
from web3 import Web3
from web3.middleware import geth_poa_middleware

# TODO: replace API-KEY with your INFURA token
json_rpc_url='https://optimism-sepolia.infura.io/v3/5920f4948d2e4fe285fc71780ff1562e'

# Connect to an Ethereum node. Replace json_rpc_url with your Infura URL or your Ethereum node URL.
web3 = Web3(Web3.HTTPProvider(json_rpc_url))
print(f"Connected to blockchain, chain id is {web3.eth.chain_id}. the latest block is {web3.eth.block_number:,}")

# Inject the PoA compatibility middleware to the innermost layer
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Read and setup a local private key
private_key = os.environ.get("PRIVATE_KEY")
print(f"Private key is {private_key}")
assert private_key is not None, "You must set PRIVATE_KEY environment variable"

# Use the Account module to derive the address
account = web3.eth.account.from_key(private_key)
sender_address = account.address
receiver_address = '0x86De8AF44476037f544C8349b1309B188f47CCdc'

print(f"Wallet Address: {sender_address}")

# Amount of ETH to send, converted to Wei. Here sending 0.01 ETH as an example.
amount_in_wei = web3.to_wei(0.0005, 'ether')

# Building the transaction
nonce = web3.eth.get_transaction_count(sender_address)
transaction = {
    'to': receiver_address,
    'value': amount_in_wei,
    'gas': 21000,  # 21000 is the gas limit for standard Ether transactions
    'gasPrice': web3.eth.gas_price,  # Get current gas price
    'nonce': nonce,
    'chainId': web3.eth.chain_id  # Ensure you're using the correct chain ID
}

# Signing the transaction
signed_txn = web3.eth.account.sign_transaction(transaction, private_key)
print(f'Sign tx: {signed_txn.rawTransaction.hex()}')

# Sending the transaction
tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

# Getting the transaction hash
explorer_url = 'https://sepolia-optimism.etherscan.io/tx/'
print(f'Transaction sent with hash: {explorer_url}{tx_hash.hex()}')