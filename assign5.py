#!/usr/bin/env python

# 2. Write a python script to help monitor the health of your /etc/passwd file.
# - Find any entries that have UID 0.
# - Find any entries that have no password (needs /etc/shadow).
# - Find any sets of entries that have duplicate UIDs.
# - Find any entries that have no expiration date (needs /etc/shadow).

# This is how your program will be run:

# python assign5.py


import os
import subprocess
from subprocess import call

print "Check for root uid..."
print call(['awk', '-F: { print $1 " " $3 }', '/etc/passwd'])

print "Check for duplicate UID's..."
print call(['awk', '-F: uname[$3]++ && uname[$3]>1 {print "duplicate user:", $1} ', '/etc/passwd'])
print "Duplicate UID check done"

print "Check for duplicate user names..."
print call(['awk', '-F: uid[$3]++ && uid[$3]>1 {print "duplicate uid:", $3}', '/etc/passwd'])
print "Duplicate user name check done."
print "Check for passwords..."

print call(['awk -F:', '($2 == "") {print $1}', '/etc/shadow'])

