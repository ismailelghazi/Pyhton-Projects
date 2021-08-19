alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
true=0
while  not true:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def crypt(text, shift):
        crypt_text = ""
        for i in text:
            pos = alphabet.index(i)
            new_index = shift+pos
            crypt_text += alphabet[new_index]
        print(crypt_text)
    def decrypt(crypt_text, shift):
        decrt_text=""
        for s in crypt_text:
            pos1=alphabet.index(s)
            old_index=pos1-shift
            decrt_text+=alphabet[old_index]
        print(decrt_text)
    if direction=="decode":

        decrypt(text, shift)
    else:
        crypt(text,shift)
    true=int(input("0-stay 1-Exit"))