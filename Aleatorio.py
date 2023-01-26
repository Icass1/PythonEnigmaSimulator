from random import randrange
from bisect import bisect, insort
from time import sleep

a = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","Á","É","Í","Ó","Ú","á","é","í","ó","ú","1","2","3","4","5","6","7","8","9",".",",","_","-","+","*","/","¿","?")
string = ""
memory = []

def number_to_letter(number):
    number -=1
    out = a[number]
    return out



while True:
    memory = []
    string = ""
    input("Enter anything: ")
    while len(memory) != 82:
        random = randrange(82)
        if random not in memory:
            memory.append(random+1)
            string += '"' + number_to_letter(number=random) + '"' + ","
    print(string)
    print("\n")


