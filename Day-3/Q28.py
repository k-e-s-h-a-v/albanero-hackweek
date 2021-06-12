'''
Q28. Parity bits are used as a very simple checksum to ensure that 
binary data isn't corrupted during transit. Here's how they work:

  If a binary string has an odd number of 1's, the parity bit is a 1.
  If a binary string has an even number of 1's, the parity bit is a 0.
  The parity bit is appended to the end of the binary string.
  Write a program that adds the correct parity bit to a binary string.

  Examples
    ("1011011") ➞ "10110111"
    // There are five 1's.
    // Since five is odd, the parity bit should be a 1.
    // Add the parity bit to the end of the string.
    // Return the result.

    ("0110000") ➞ "01100000"

    ("0101101") ➞ "01011010"

    ("1111111") ➞ "11111111"
  Notes
    All inputs will be 7-bits long (so that the parity bit makes it a full byte).
'''

def parityCheck(strng):
    count = 0
    for i in strng:
        if i=='1':
            count += 1
    if count%2:
        return strng+'1'
    else:
        return strng+'0'

Examples = ["0110000", "0101101", "1111111"]
for example in Examples:
    print('for', example,'➞',parityCheck(example))