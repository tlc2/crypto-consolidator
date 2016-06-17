# crypto-consolidator
simple python script to consolidate eg. mining/masternode inputs into one address

usage: 

1. clone or copy cc.py, save it to wherever your wallet lives and make sure bitcredit-cli/bitcoin-cli/dash-cli or whatever is in the same directory

2. modify line #13 to yourcurrency-cli if needed

3. start bitcredit-qt or bitcreditd, and in your wallet console or on the CLI, run 'listaccounts' to see what you're working with

4. create a new recieving account with 'getaccount label' or the receive request GUI dialog

5. unlock your wallet, run dumpprivkey for the address you're consolidating to and copy and keep that privkey safe!

6. your wallet must be unlocked for the script to work, so unlock your wallet for an appropriate amount of time, eg. 1000 secs or something, depends how many txes you have to consolidate

7. run with 'python cc.py fromaccount toaddress amount'
eg. python cc.py "" 6By49FGYf15SQUweCF4ieya67321GiJ7mP 1000

experiment with amount for best results for your wallet situation, keep rerunning script until your BCR are where you want them
