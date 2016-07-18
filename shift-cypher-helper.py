import string
chars = list(string.ascii_lowercase)
shift = 2

print("\nShift: " + str(shift) + ' (set this in program)\n')

for i in range(0, 26):
    print(str(i) +': '+ chars[i] +'\t-->\t'+
          str( (i+shift)%26 )+': '+chars[(i+shift)%26])
