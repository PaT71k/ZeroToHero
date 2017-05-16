import string
alphabet = string.ascii_lowercase

def pangramCheck(str):
    for a in alphabet:
        if a not in str:
            return False
    return True

inputStr = input("Upiši rečenicu: ")

print( pangramCheck(inputStr.lower()) )
