from bisect import bisect, insort
from random import randrange, shuffle
from time import sleep
from typing import SupportsFloat

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","Á","É","Í","Ó","Ú","á","é","í","ó","ú","1","2","3","4","5","6","7","8","9",".",","," ","-","+","*","/","¿","?"]

long_alphabet =    ['☺', '☻', '♥', '♦', '♣', '♠', '•', '◘', '○', '◙', '♂', '♀', '♪', '♫', '☼', '►', '◄', '↕', '‼', '¶', '§', '▬', '↨', '↑', '↓', '→', '←', '∟', '↔', '▲', '▼', 'A', '"', '#', '$', 
'%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
'V', 'W', 'X', 'Y', 'Z', '[', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}',
'~', 'Δ', '€', '‚', 'ƒ', '„', '…', '†', '‡', 'ˆ', '‰', 'Š', '‹', 'Œ', 'Ž', '‘', '’', '“', '”', '•', '–', '—', '˜', '™', 'š', '›', 'œ', 'ž', 'Ÿ', '¡', '¢', '£', '¤', '¥', '¦', '§', '¨', '©', 'ª',
'«', '¬', '®', '¯', '°', '±', '²', '³', '´', 'µ', '¶', '·', '¸', '¹', 'º', '»', '¼', '½', '¾', '¿', 'À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò',
'Ó', 'Ô', 'Õ', 'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', '÷', 'ø', 'ù',
'ú', 'û', 'ü', 'ý', 'þ', 'ÿ', 'Ç', 'ü', 'é', 'â', 'ä', 'à', 'å', 'ç', 'ê', 'ë', 'è', 'ï', 'î', 'ì', 'Ä', 'Å', 'É', 'æ', 'Æ', 'ô', 'ö', 'ò', 'û', 'ù', 'ÿ', 'Ö', 'Ü', '¢', '£', '¥', '₧', 'ƒ', 'á',
'í', 'ó', 'ú', 'ñ', 'Ñ', 'ª', 'º', '¿', '⌐', '¬', '½', '¼', '¡', '«', '»', '░', '▒', '▓', '│', '┤', '╡', '╢', '╖', '╕', '╣', '║', '╗', '╝', '╜', '╛', '┐', '└', '┴', '┬', '├', '─', '┼', '╞', '╟',
'╚', '╔', '╩', '╦', '╠', '═', '╬', '╧', '╨', '╤', '╥', '╙', '╘', '╒', '╓', '╫', '╪', '┘', '┌', '█', '▄', '▌', '▐', '▀', 'α', 'ß', 'Γ', 'π', 'Σ', 'σ', 'µ', 'τ', 'Φ', 'Θ', 'Ω', 'δ', '∞', 'φ', 'ε',
'∩', '≡', '±', '≥', '≤', '⌠', '⌡', '÷', '≈', '°', '∙', '·', '√', 'ⁿ', '²', '■', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']

def char_is_in_list(char, list):
    for k in list:
        if char == k:
            return True
    return False

def _pop(index, list):
    _out = []
    for element in list:
        if list.index(element) == index:
            pass
        else: _out.append(element)
    return _out

def generata_pairs(alphabet):
    print(len(alphabet))
    list_1 = alphabet
    list_2 = []
    for k in list_1:
        list_2.append("ą")

    characters_left = alphabet
    for letter in list_1:
        print(letter)

        if char_is_in_list(char=letter, list=list_2):
            _index = list_2.index(letter)
            list_2[list_1.index(letter)] = list_1[_index]
            characters_left = _pop(index=_index, list=characters_left)
            print("if")
        else:
            print("else")
            random_number = randrange(len(characters_left) - 1)
            random_letter = characters_left[random_number]
            list_2[list_1.index(letter)] = random_letter

            characters_left = _pop(index=random_number, list=characters_left)

        
        print(list_1)
        print(list_2)
        print(characters_left)            
        print("\n")
    print(list_1)
    print("\n")
    print(list_2)
    return list_1, list_2

def check_pairs(list_1, list_2):
    if len(list_1) != len(list_2):
        print("The length of the lists must be equal.")
        return
    for _index in range(0, len(list_1) - 1):
        list_1_letter_1 = list_1[_index]
        list_2_letter_1 = list_1[_index]
        
        list_1_letter_2 = list_1[list_2.index(list_1_letter_1)]
        list_2_letter_2 = list_2[list_1.index(list_2_letter_1)]
        print(list_1_letter_1)
        print(list_2_letter_1)
        print(list_1_letter_2)
        print(list_2_letter_2)

list_1, list_2 = generata_pairs(alphabet=alphabet)
check_pairs(list_1=list_1, list_2=list_2)

