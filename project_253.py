# --------------253 Proj----------------
from web3 import Web3
# Import time module here
 

ganache_url = 'http://127.0.0.1:7545'

web3_ganache_connection = Web3(Web3.HTTPProvider(ganache_url))

Alice_account = 'Paste 1st address here'
James_account = 'Paste 2nd address here'
Ryan_account  = 'Paste 3rd address here'


nonce1 = web3_ganache_connection.eth.getTransactionCount("Add sender account variable here")

transaction_data1 = {
    'nonce':"Add the nonce2 here",
    'to':"Add James_account here",
    'value':web3_ganache_connection.toWei("Enter the Ether Amount need to transfer", 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.toWei(50,'gwei')
}

private_key1 = 'Write the Private Key of sender'

singed_transaction1 = web3_ganache_connection.eth.account.signTransaction(transaction_data1,private_key1)
transaction_hash1 = web3_ganache_connection.eth.sendRawTransaction(singed_transaction1.rawTransaction)

print(web3_ganache_connection.toHex("Print the Hash of the Block 1 here"))



# -----------------
"Define the print statement and" 
"sleep() function here"
# -----------------



nonce2 = web3_ganache_connection.eth.getTransactionCount("Add sender account variable here")

transaction_data2 = {
    'nonce':"Add the nonce2 here",
    'to':"Add Ryan_account here",
    'value':web3_ganache_connection.toWei("Enter the Ether Amount need to transfer", 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.toWei(40,'gwei')
}

private_key2 = 'Write the Private Key of sender'

singed_transaction2 = web3_ganache_connection.eth.account.signTransaction(transaction_data2,private_key2)
transaction_hash2 = web3_ganache_connection.eth.sendRawTransaction(singed_transaction2.rawTransaction)

print(web3_ganache_connection.toHex("Print the Hash of the Block 2 here"))



