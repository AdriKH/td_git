print("entrer votre texte")
text = input("texte\t")
print("que souhaitez-vous faire?")
print("taper C si vous souhaitez transformer un texte de manière à ce que l'on enlève tous les caractères spéciaux ET qu'on enlève les accents. On voudra aussi transformer un texte et l'écrire en majuscules.\n")
print("taper D si vous souhaitez prendre deux textes en entrée et de savoir si au moins une phrase d'un texte a été recopiée dans l'autre texte.\n")
print("taper C si vous souhaitez réaliser facilement plusieurs traitements sur un texte.\n")
print("taper D si vous souhaitez chiffrer un texte sans espace et sans caractères spéciaux et en majuscules à l'aide du code de César.\n")
print("taper C si vous souhaitez chiffrer un texte avec le chiffre de Vigenere.\n")
lettre= input("faites votre choix\t")

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