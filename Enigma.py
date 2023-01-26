from random import randrange
import time

from rotors import get_sources

counter_invalid_letter = 0

encripted_letters = []

start_encript = []

# Set alphabet. 

sources = get_sources()
alphabet = sources[0]

# Returns the letter that is in the posiiton of number in source.
def number_to_letter(source, number):
    return source[number]

# Returns the number of the position of letter in source.
def letter_to_number(source, letter):
    return source.index(letter)

def encript(message):
    rotors_position = []
    for k in range(int((len(sources) - 1)/2)): rotors_position.append(None)

    counter_for_position_rotors_input = 0

    # If the input has the initial letters of the rotors, remove them from the input and set them as the position of the rotors.
    if len(message) > (len(sources) - 1):
        for k in range(int(len(sources)/2)):
            k *= 2
            if message[k] in alphabet:
                counter_for_position_rotors_input += 1
            if message[k+1] == " ":
                counter_for_position_rotors_input += 1
        if counter_for_position_rotors_input == (len(sources)-1):
            
            for k in range(int(len(sources)/2)): rotors_position[k] = letter_to_number(letter=message[k*2], source=alphabet)
            message = message[(len(sources) - 1):len(message)]
            
        else:
            for k in range(int(len(sources)/2)): rotors_position[k] = randrange(len(alphabet)-1)
    else:
        for k in range(int(len(sources)/2)): rotors_position[k] = randrange(len(alphabet)-1)

    # Write the initial position of the rotors in _out.
    _out = ""
    # _out += number_to_letter(source=alphabet, number=rotors_position[0]) + " " + number_to_letter(source=alphabet, number=rotors_position[1]) + " " + number_to_letter(source=alphabet, number=rotors_position[2]) + " "
    
    for k in range(int(len(sources)/2)):
        _out += number_to_letter(source=alphabet, number=rotors_position[k]) + " "

    _max = len(alphabet) - 1
    _min = 0
    _add_substract = len(alphabet)

    for_rotors = int((len(sources)-1)/2-1)

    # Encript each letter of the input one by one.
    for letter in message:
        if letter in alphabet:
            number = int(letter_to_number(source=alphabet, letter=letter))
            number -= rotors_position[0]
            number += 1

            if number > _max: number -= _add_substract
            elif number < _min: number += _add_substract


            for k in range(for_rotors):
                _position_add = rotors_position[k]
                _position_substract = rotors_position[k+1]
                k *= 2

                letter = number_to_letter(source=sources[k+1], number=number)
                
                number = int(letter_to_number(source=sources[k+2], letter=letter))
                number += _position_add
                number -= _position_substract

                if number > _max: number -= _add_substract
                elif number < _min: number += _add_substract

            letter = number_to_letter(source=sources[len(sources)-2], number=number)

            number = int(letter_to_number(source=sources[len(sources)-1], letter=letter))

            number += rotors_position[len(rotors_position)-1]
            number -= rotors_position[len(rotors_position)-2]

            if number > _max: number -= _add_substract
            elif number < _min: number += _add_substract

            for k in range(for_rotors, 0, -1):
                k -= 1
                _position_add = rotors_position[k]
                if k == 0:
                    _position_substract = 1

                else: _position_substract = rotors_position[k-1]

                k *= 2

                letter = number_to_letter(source=sources[k+2], number=number)
                
                number = int(letter_to_number(source=sources[k+1], letter=letter))
                number += _position_add
                number -= _position_substract

                if number > _max: number -= _add_substract
                elif number < _min: number += _add_substract

            _out += number_to_letter(source=alphabet, number=number)

        else: 
            print(letter + "is not in the alphabet")
        
        rotors_position[0] = rotors_position[0] + 1

        if rotors_position[0] == len(alphabet):
            rotors_position[0] = 0
            rotors_position[1] = rotors_position[1] + 1

        if rotors_position[1] == len(alphabet):
            rotors_position[1] = 0
            rotors_position[2] = rotors_position[2] + 1
            
        if rotors_position[2] == len(alphabet):
            rotors_position[2] = 0
        
    return _out


def test():
    while True:
        string = ""
        for _ in range(1000):
            string += alphabet[randrange(len(alphabet))]
        
        string_encripted = encript(string)

        print("***************************************")

        string_desencripted = encript(string_encripted)
        
        counter_for_position_rotors_input = 0

        if len(string_desencripted) > (len(sources) - 1):
            for k in range(int(len(sources)/2)):
                k *= 2
                if string_desencripted[k] in alphabet:
                    counter_for_position_rotors_input += 1
                if string_desencripted[k+1] == " ":
                    counter_for_position_rotors_input += 1
            if counter_for_position_rotors_input == (len(sources)-1):
                string_desencripted = string_desencripted[(len(sources) - 1):len(string_desencripted)]
            
        if string_desencripted != string:
            print("string             ", string)
            print("string_desencripted", string_desencripted)
        else:

            print("[ CORRECT ]")
        print("")
        time.sleep(0.01)
        
#test()

while True:
    _input = input("Enter message: ")
    message_encripted = encript(message=_input)
    print(message_encripted)
