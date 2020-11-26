# Ceaser_cipher
# Section 5.1.11.6
text = input("Enter your message: ")
cipher = ''
s = int(input("shift value: "))

for char in text:

    if char.isupper():
        cipher += chr((ord(char) + s - 65) % 26 + 65)
    # Encrypt lowercase characters in plain text
    elif char.islower():
        cipher += chr((ord(char) + s - 97) % 26 + 97)
    else:
        cipher += char

print(cipher)
