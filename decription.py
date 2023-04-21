# Program was originally created on Thursday, April 05, 2023.

print("Hello! What shall we decrypt today?")
encrypted_text = input("Enter the message to be decrypted: ")

# Decrypt it using the program

decrypted_text = encrypted_text.replace("*", "a").replace("&","e").replace("#", "i").replace("+", "o").replace("!", "u")

# Print the output

print("Your encrypted text was " + encrypted_text)
print("The decrypted message is " + decrypted_text)

