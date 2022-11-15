print("entrer votre texte")
text = input("texte")

def upCase(text):
    text = text.upper()
    pass

letters = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

def deleteCaracter(text):
    for i in range(len(text)):
        for j in range(len(letters)):
            if text[i] == letters[j]:
                break
            else:
                text[i] = charSpe(text[i])
    pass

def charSpe(char):
    if char == "é" or char == "ê" or char == "ë":
        char = "e"
    elif char == "à" or char == "â" or char == "ä":
        char = "a"        
    return char

deleteCaracter(text)
print(text)
