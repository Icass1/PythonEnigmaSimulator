from bisect import bisect, insort
from random import random, randrange, shuffle
from time import sleep
from typing import SupportsFloat

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","Á","É","Í","Ó","Ú","á","é","í","ó","ú","1","2","3","4","5","6","7","8","9",".",","," ","-","+","*","/","¿","?"]

long_alphabet =    ['☺', '☻', '♥', '♦', '♣', '♠', '•', '◘', '○', '◙', '♂', '♀', '♪', '♫', '☼', '►', '◄', '↕', '‼', '¶', '§', '▬', '↨', '↑', '↓', '→', '←', '∟', '↔', '▲', '▼', 'A', '"', '#', '$',
'%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
'W', 'X', 'Y', 'Z', '[', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'Δ', '€', '‚', 'ƒ', '„', '…', '†', '‡', 'ˆ', '‰', 'Š', '‹', 'Œ', 'Ž', '‘', '’', '“', '”', '–', '—', '˜', '™', 'š', '›', 'œ', 'ž', 'Ÿ', '¡', '¢', '£', '¤', '¥', '¦', '¨', '©', 'ª', '«', '¬', '®',
'¯', '°', '±', '²', '³', '´', 'µ', '·', '¸', '¹', 'º', '»', '¼', '½', '¾', '¿', 'À', 'Á', 'Â', 'Ã', 'Ä', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', '×',
'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', '÷', 'ø', 'ù', 'ú', 'û', 'ü', 'ý', 'þ',
'ÿ', 'Å', '₧', '⌐', '░', '▒', '▓', '│', '┤', '╡', '╢', '╖', '╕', '╣', '║', '╗', '╝', '╜', '╛', '┐', '└', '┴', '┬', '├', '─', '┼', '╞', '╟', '╚', '╔', '╩', '╦', '╠', '═', '╬', '╧', '╨', '╤', '╥',
'╙', '╘', '╒', '╓', '╫', '╪', '┘', '┌', '█', '▄', '▌', '▐', '▀', 'α', 'Γ', 'π', 'Σ', 'σ', 'τ', 'Φ', 'Θ', 'Ω', 'δ', '∞', 'φ', 'ε', '∩', '≡', '≥', '≤', '⌠', '⌡', '≈', '∙', '√', 'ⁿ', '■', '1', '2',
'3', '4', '5', '6', '7', '8', '9', ' ']


def _pop(index, list):
    _out = []
    for element in list:
        if list.index(element) == index:
            pass
        else: _out.append(element)
    return _out

def check(list):
    valores = list
    repetido = []
    unico = []
    for x in valores:
        if x not in unico:
            unico.append(x)
        else:
            if x not in repetido:
                repetido.append(x)

def generata_pairs(alphabet):
    global list_pairs
    _list = alphabet

    list_pairs = []
    while len(_list) != 0:
        random_number = randrange(len(_list))
        random_leter = _list[random_number]



        list_to_append = [_list[0], random_leter]
        list_pairs.append(list_to_append)
        _list = _pop(index=0, list=_list)

        try: _list = _pop(index=_list.index(random_leter), list=_list)
        except: pass

    # print(len(list_pairs)) 

    list_1 = []
    list_2 = []
    for pair in list_pairs:
        if pair[0] == pair[1]:
            list_1.append(pair[0])
            list_2.append(pair[1])
        else:
            list_1.append(pair[0])
            list_1.append(pair[1])

            list_2.append(pair[1])
            list_2.append(pair[0])
    return list_1, list_2

list_1, list_2 = generata_pairs(alphabet=long_alphabet)

print("alphabet =                  ({})".format(str(long_alphabet).replace("[", "").replace("]", "")))
print("\n")
shuffle(long_alphabet)
print("_alpha_rotor_external =     ({})".format(str(long_alphabet).replace("[", "").replace("]", "")))
print("\n")
shuffle(long_alphabet)
print("_alpha_rotor_internal =     ({})".format(str(long_alphabet).replace("[", "").replace("]", "")))
print("\n")
shuffle(long_alphabet)
print("_beta_rotor_external =      ({})".format(str(long_alphabet).replace("[", "").replace("]", "")))
print("\n")
shuffle(long_alphabet)
print("_beta_rotor_internal =      ({})".format(str(long_alphabet).replace("[", "").replace("]", "")))
print("\n")
print("_reflector_rotor_external = ({})".format(str(list_1).replace("[", "").replace("]", "")))
print("\n")
print("_reflector_rotor_internal = ({})".format(str(list_2).replace("[", "").replace("]", "")))

