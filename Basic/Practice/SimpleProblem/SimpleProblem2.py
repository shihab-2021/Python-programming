""" 
Encrypt the following code so that no one can get your strategy.
"""
data = 'fire'

shift = 1
output1 = ''
output2 = ''

# converting in secret
for character in data:
    output1 += chr((ord(character) + shift - 97) % 26 +97)

print(output1)

for character in output1:
    output2 += chr((ord(character) - shift - 97) % 26 +97)

print(output2)