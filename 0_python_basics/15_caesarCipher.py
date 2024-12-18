# functions must be defined before they are called
def encrypt(msg, shift):
    encrypted = ""
    for letter in msg:
        if letter.isalpha():
            # change base according to letter
            base = ord("a") if letter.isupper() else ord("A")
            letter = (ord(letter) + shift - base) % 26 + base
            encrypted = encrypted + chr(letter)
        else:
            # non character
            encrypted = encrypted + letter
    print(f"Here's the encrypted result: {encrypted}")


def decrypt(msg, shift):
    decrypted = ""
    for letter in msg:
        if letter.isalpha():
            # change base according to letter
            base = ord("a") if letter.isupper() else ord("A")
            letter = (ord(letter) - shift - base) % 26 + base
            decrypted = decrypted + chr(letter)
        else:
            decrypted = decrypted + letter
    print(f"Here's the decrypted result: {decrypted}")


flag = True
while flag:
    type = input(
        "Type \"encrypt\" for encryption, type \"decrypt\" for decryption: ").strip().lower()
    # edge case handling
    if type not in ["encrypt", "decrypt"]:
        print("try again")
        continue
    msg = input("Type your message: ").strip()
    # exception handling
    try:
        shift = int(input("Type the shift number").strip())
    except ValueError:
        print("Invalid shift nuber")
        continue
    if type == "encrypt":
        encrypt(msg, shift)
    else:
        decrypt(msg, shift)
    con = input("Type \"yes\" if you want to go again, Otherwise type \"no\"")
    if con == "no":
        flag = False
