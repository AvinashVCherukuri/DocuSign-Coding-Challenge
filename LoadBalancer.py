"""
Program Name: LoadBalancer.py
Program Purpose: DocuSign Coding Challenge
This Python Program gives the name of the server that can process incoming document based on server load capacity.

Input: Takes command line arguments in the format of ServerName:LoadCapacity. For example: A:7 or V:3 I:5.
Output: Prints a Weighted Random ServerName based on user input of LoadCapacity.

Execution: Use python3 interpreter for running the code. You can give any number of arguments. Example 1 - python3 LoadBalancer.py A:7 V:3 Example 2 - python3 LoadBalancer.py H:2 E:6 Y:9

LinkedIn Profile: https://www.linkedin.com/in/avinashvarmacherukuri/
Code: https://github.com/AvinashVCherukuri/DocuSign-Coding-Challenge.git
"""

import re 		  # Package used for String Pattern Matching
import sys 		  # Package used for reading Command Line Arguments
import random 	  # Package used for generating a Weighted Random Choice using a list of weights 


# Validate the input for correct format. Check for both Null values and inconsistencies.
# Verify for atleast one input value.
if len(sys.argv) == 1 :
	print("\n\tThis programs requires a minimum of 1 command line argument to function.\n\tFor example: python3 LoadBalancer.py A:7\n\tor python3 LoadBalancer.py A:7 V:3\n")
	exit(0)


Servers = {}		# Initializing an empty dictionary


# Verify weather each argument is in the right format of ServerName:LoadCapacity. 
# If any of the arguments are not in the correct format then exit the progam exits and promt the user to give the right input.
# Otherwise store each argument in the Servers dictionary
for argument in sys.argv [1 : len(sys.argv)] :

	if re.match(r'(.+):\d', argument) == None :
		print("\n\tPlease give input in the format of ServerName:LoadCapacity\n\tFor example: python3 LoadBalancer.py A:7\n\tor python3 LoadBalancer.py A:7 V:3\n")

	else :
		ServerName,LoadCapacity = argument.split(":")
		Servers.update({ ServerName : int(LoadCapacity)})


# Use dictionary comprehension to convert LoadCapacity of each of the servers to percentages.
Servers = { key : (value/sum(Servers.values())) for key, value in Servers.items() }


# Send two arguments, ServerNames and LoadCapacity-percentages to random.choice built in method 
# to print weighted random servername in the form of a string.
print(*random.choices(list(Servers.keys()), list(Servers.values())))