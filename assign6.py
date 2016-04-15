#!/usr/bin/env python
import os
import sys

# Read input from command line
input_file = sys.argv[1]
file = open(input_file)
data = file.readlines()
file.close()
print data