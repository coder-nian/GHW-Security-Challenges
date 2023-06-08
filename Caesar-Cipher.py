def caesar_cipher(plainText, key):
  cipheredText = ""

  # Iterate through each character in the text
  for char in plainText:
    # Check if the character is a letter
    if char.isalpha():
      # Get the Unicode code of the character
      unicode_val = ord(char)

      # Determine the appropriate rotations based on the case (uppercase or lowercase)
      if char.isupper():
        # Ensuring that the key value is within the range of 26
        key = key % 26 
        unicode_val = (unicode_val - 65 + key) % 26 + 65
      else:
        # Ensuring that the key value is within the range of 26
        key = key % 26
        unicode_val = (unicode_val - 97 + key) % 26 + 97

      # Convert the Unicode code back to a character and add it to the cipheredText
      cipheredText += chr(unicode_val)
    else:
      # If the character is not a letter, add it to the cipheredText as it is
      cipheredText += char

  return cipheredText

#Taking Input from the user
unencryptedText = input("Enter yout text: ")
key = int(input("Enter your key: "))
encryptedText = caesar_cipher(unencryptedText, key)

print("Encrypted Text: ", encryptedText)
