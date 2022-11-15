def upCase(text):
    text = text.upper()
    pass

def deleteCaracter(text):
    for i in range(text.len()):
        charSpe(text[i])
    pass

def charSpe(char):
    if char == "é" or char == "ê":
        return char = "e"
