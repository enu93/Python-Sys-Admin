#!/usr/bin/env python
import os
import sys
import crypt

def createUser(firstName, lastName, password, uid, gid):
	fname = firstName[:1].lower()
	lname = lastName[:7].lower()
	name = fname + lname
	encPass = crypt.crypt(password,"s3")
	return os.system("useradd -p "+encPass+" -u "+uid+" -g "+gid+" "+name)
	
# Read input from command line
input_file = sys.argv[1]
file = open(input_file)
data = file.read().splitlines()
file.close()

for data in data:
	input_data = data.split(";")
	firstName = input_data[0]
	lastName = input_data[1]
	password = input_data[2]
	uid = input_data[3]
	gid = input_data[4]
	createUser(firstName,lastName, password, uid, gid)
