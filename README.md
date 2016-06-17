# crypto-consolidator
simple python script to consolidate eg. mining/masternode inputs into one address

usage: 

clone or copy cc.py 

modify line #13 to yourcurrency-cli if needed

in your wallet console, run 'listaccounts' to see what you're working with

create a new recieving account with 'getaccount label'

run with 'python cc.py fromaccount toaddress amount'

eg. python cc.py "" 6By49FGYf15SQUweCF4ieya67321GiJ7mP 1000

experiment with amount for best results for your wallet situation
