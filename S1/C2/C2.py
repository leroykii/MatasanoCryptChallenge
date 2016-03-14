#!/usr/bin/env python3
# Write a function that takes two equal-length buffers and produces their XOR combination.

import binascii
import sys
import base64

#sys.path.insert(0, '../')
#from repoC1 import countLetters
#from repoC1 import divisiblebythree

# Output
sExpected = "746865206b696420646f6e277420706c6179"

# Input
sInput = "1c0111001f010100061a024b53535009181c"

# Mask
sXORmask = "686974207468652062756c6c277320657965"

print("Input:", sInput)
print("Mask:", sXORmask)

#################################################

iInput = int(sInput, 16)
iXORmask = int(sXORmask, 16)

iOutput = iInput ^ iXORmask
hOutput = hex(iOutput)[2:]

#################################################

print("Output:", hOutput)

# Test if challenged passed.
if (hOutput == sExpected):
    print("Challenge Done!! :D :D")
else:
	print("Challenge Failed... Keep trying! =)")




