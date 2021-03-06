import string
chars = list(string.ascii_lowercase)
shift = 11

print("\nShift: " + str(shift) + ' (set this in program)\n')

# print shift table for easier shift decryption by hand
for i in range(0, 26):
    print(str(i) +': '+ chars[i] +'\t-->\t'+
          str( (i+shift)%26 )+': '+chars[(i+shift)%26])

print('\n\n')

# x - plaintext
# y - encrypted text
x = ''
y = list('xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpitghlxiwiwtxgqadds')

# decrypt/build plaintext string
for char in y:
    x+=chars[(chars.index(char)+shift)%26]

# print the plaintext
print('y = '+ ''.join(y) +'\n')
print('x = '+ x)

# Letter Frequency Letter Frequency
# A 0.0817         N 0.0675
# B 0.0150         O 0.0751
# C 0.0278         P 0.0193
# D 0.0425         Q 0.0010
# E 0.1270         R 0.0599
# F 0.0223         S 0.0633
# G 0.0202         T 0.0906
# H 0.0609         U 0.0276
# I 0.0697         V 0.0098
# J 0.0015         W 0.0236
# K 0.0077         X 0.0015
# L 0.0403         Y 0.0197
# M 0.0241         Z 0.0007
