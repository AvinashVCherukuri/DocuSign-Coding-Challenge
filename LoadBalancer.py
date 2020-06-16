"""
DocuSign - Coding Challenge
Python Program to calculate the next server to process incoming document based on server load capacity.

Avinash Varma - https://www.linkedin.com/in/avinashvarmacherukuri/
Code - https://github.com/AvinashVCherukuri/DocuSign-Coding-Challenge.git
"""

import re
import sys
import random


# We do 2 checks to see if the input is fullfiling our requirement or not. 
# Check 1 is to see if the input is null or not.
if len(sys.argv) == 1 :
	print("\nHey!\tThis programs requires a minimum of 1 command line argument to function.\n\tExample: python3 LoadBalancer.py A:7 V:3\n")
	exit(0)


# Check 2 is to see if the input is formatted in the right way or not
if re.match(r'(.+):(.+)', sys.argv[1]) == None :
	print("\nHey!\tPlease give input in the format of ServerName:LoadCapacity\n\tExample: python3 LoadBalancer.py A:7 V:3\n")
	exit(0)


# Dictionary Comprehension to store ServerName and its LoadCapacity value in "Servers"
Servers = { argument[0] : int(argument[2]) for argument in sys.argv [1 : len(sys.argv)] }


# Dictionary Comprehension converts the LoadCapacity in Servers to percentages
Servers = { key : (value/sum(Servers.values())) for key, value in Servers.items() }


# Stores a weighted random number using the percentages from Servers in the form of a list
Choice = random.choices(list(Servers.keys()), list(Servers.values()))


# Prints the Choice in the form of a string
print(*Choice)