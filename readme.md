# AI Agents


## Preparation of wallet for Optimism transaction

1. add chain RPC endpoint to Metamask
    We use Optimism Sepolia testnet.
    https://chainlist.org/chain/11155420

2. Get INFRA API KEY
    create your account and get HTTP API endpoint of RPC. 

## Demonstration of Optimism token transfer

[token_transfer.py](./src/optimism/token_transfer.py) is a script to demonstrate transferring Optimism Sepolia testnet token between 2 wallets.  

1. Set up Private key of `sender_wallet`.  
    Private key should start from `0xs092349....sa89` prefix.  
    You can get privatekey information from account details of Metamask.
    ```.bash
    export PRIVATEKEY='0x' 
    ```
2. Switch INFURA API KEY to yours.

3. Set up the sender address.

4. Change the amount of token you sent from `receiver_address` to `sender_address`.


5. try `poetry run python token_transfer.py`. You can get teh result like below.

    ```
    Connected to blockchain, chain id is 11155420. the latest block is 9,429,352
    Private key is 0x5966e34713454fcda8031dcb20ddc39cb82fc7689bb87480559e54b470d8cae3
    Wallet Address: 0x39f3b9C8585Fc57A57EC39322E92Face43484D97
    Sign tx: 0xf86d02830f433c8252089486de8af44476037f544c8349b1309b188f47ccdc8701c6bf52634000808401546fdca079066bddab380a6a2797ca90b21568c716f10be769fd55aabd4478ab83acc4d8a03db1252c0e66f202d918411c7d2cf1595dc39f56933cc5d809e6a38ceda459fa
    Transaction sent with hash: https://sepolia-optimism.etherscan.io/tx/0x40635010b0426729223e364c19100ef90485733813d20001d4fd5c5071ba77bc
    ```