# crypto-consolidator
simple python script to consolidate eg. mining/masternode inputs into one address, should work with any bitcoin-derived currency, example usage here pertains to bitcredit

usage (ENTIRELY AT YOUR OWN RISK!): 

1. clone or copy cc.py, save it to wherever your wallet lives and make sure bitcredit-cli or whatever is in the same directory

2. create a fresh wallet to consolidate to, encrypt it, restart it, enter passphrase and dumpprivkey of fresh receiving address, backup and keep safe this privkey, also backup wallet.dat file

3. close bitcredit-qt or bitcreditd, swap in your bloated old wallet and restart

4. your wallet must be unlocked for the script to work, so unlock your wallet for an appropriate amount of time, eg. 1000 secs or something, depends how many txes you have to consolidate

5. run with 'python cc.py currency toaddress amount'

eg. 

python cc.py bitcredit 6By49FGYf15SQUweCF4ieya67321GiJ7mP 1000


the script will keep on repeating that transaction until you've run out of funds or it can't build that amount from the available inputs

experiment with amount for best results for your wallet situation, keep rerunning script until your BCR are where you want them, eg. after consolidating in chunks of n, repeat in chunks of 10*n or whatever suits you

Licence: http://www.wtfpl.net/
