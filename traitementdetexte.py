print("entrer votre texte")
input("texte")

def upCase(text):
    text = text.upper()
    pass

def deleteCaracter(text):
    for i in range(text.len()):
        charSpe(text[i])
    pass

def charSpe(char):
    if char == "é" or char == "ê" or char == "ë":
        char = "e"
    elif char == "à" or char == "â" or char == "ä":
        char = "a"        
    return char