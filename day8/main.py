alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt(text, shift):

  encri_word=""
  for i in text:
    pos=alphabet.index(i)

    i=alphabet[pos+shift]
    encri_word+=i
  print(f"The encoded text is {encri_word}")


def decrypt(text, shift):


  dencri_word=""
  for i in text:
    pos=alphabet.index(i)

    i=alphabet[pos-shift]
    dencri_word+=i
  print(f"The decoded text is {dencri_word}")


if direction=="encode":
  print(encrypt(text,shift))
elif direction=="decode":
  print(decrypt(text,shift))
else:
  print("asignación no válida")

