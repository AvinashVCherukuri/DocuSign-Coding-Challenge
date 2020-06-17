# DocuSign Coding Challenge

Program Name -

	LoadBalancer.py


Program By -

	Avinash Varma
	LinkedIn: https://www.linkedin.com/in/avinashvarmacherukuri/


Program Description -

	The Python Program gives the name of the server that can process incoming document based on server load capacity.


Input -

	Takes command line arguments in the format of ServerName:LoadCapacity. 
	For example: A:7 or V:3 I:5.


Output -

	Prints a Weighted Random ServerName based on user input of LoadCapacity.


Execution -

	Use python3 interpreter for running the code. You can give any number of arguments. 
	Example 1 - python3 LoadBalancer.py A:7 V:3 
	Example 2 - python3 LoadBalancer.py H:2 E:6 Y:9


Coding Challenge -

	DocuSign has different sized servers that process documents in its data centers. To load balance jobs across the servers, each job is assigned to a random server such that if server X is three times as big as server Y, then server X gets assigned three times as often as server Y. So server X would be assigned approximately 75% of the time and server Y would be assigned 25% of the time.

	Write a program in any programming language that takes server names and sizes as arguments and outputs the name of a random server based on the algorithm described above. For instance:

	bash-3.2$ program X:3 Y:1 X
	bash-3.2$ program X:3 Y:1 Y
	bash-3.2$ program X:3 Y:1 X
	bash-3.2$ program X:3 Y:1 X

	There can be any number of servers passed on the command-line:
	bash-3.2$ program A:3 B:2 C:4 D:4 E:1 C
	bash-3.2$ program X:3 Y:1 Z:3 X