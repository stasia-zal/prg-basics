###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''


for char in plain_text:
    number=ord(char)   # read the character's code (use ord())
    if number==32:
        number=31
    number=number +1
    # add one to the character's code
    new_char=chr(number)
    # replace new character code with its
    # corresponding character (use chr())
    encrypted_text=encrypted_text+new_char
    # add encrypted character to encrypted text
    ...

print("plain_text", plain_text)
print("encrypted_text", encrypted_text )