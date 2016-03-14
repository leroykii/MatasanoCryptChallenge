#!/usr/bin/env python
# -*- coding: utf-8 -*-
import binascii
import sys
import base64

sys.path.insert(0, '../')

from repoC1 import countLetters
from repoC1 import divisiblebythree

# Output
expected = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

# Input
s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

print("Hex String:", s)
print("Number of letters:", countLetters(s))

if (divisiblebythree(countLetters(s)) == True): print("The number of string elements is divisible by 3.")

rawbytes = bytearray.fromhex(s)
print("Hidden message:", rawbytes)

encoded_message = binascii.b2a_base64(rawbytes)
encoded_message = encoded_message.rstrip() # Remove '\n'
print("Encoded message:", encoded_message)

# Test if challenged passed.
if (encoded_message == expected):
    print("Challenge Done!! :D :D")
else:
    print("Challenge Failed... Keep trying! =)")


