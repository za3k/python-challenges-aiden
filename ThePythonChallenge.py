from typing import Optional


def lvl_0():
    ans_0 = 2**38
    print(f'lvl 0 solution: http://www.pythonchallenge.com/pc/def/{(ans_0)}.html')
    return ans_0

def read_file(text_file_name: str) -> str:
    text_file = open(text_file_name, "r")
    contents = text_file.read()
    text_file.close()
    return contents

def lvl_1():
    """Solve the lvl 1 puzzle (at http://www.pythonchallenge.com/pc/def/map.html) and print the url to lvl 2"""
    cryptic_string = read_file("lvl1.txt")
    new_string = shift_string(cryptic_string,2)
    print(f'lvl 1 decoded hint: {new_string}')
    # Hint says to shift the URL!
    # The original url is http://www.pythonchallenge.com/pc/def/map.html
    # The correct part to shift is just                         ^^^
    ans_1 = shift_string('map',2)
    print(f'lvl 1 solution: http://www.pythonchallenge.com/pc/def/{ans_1}.html')

def shift_letter(letter : str , shift_forward : int) -> str:
    """Ex. shifting A forward by 2 gives C"""
    number = letter_to_number(letter) # Ex. C -> 3
    number += shift_forward
    #if number > 25:
    #    number = number - 26
    number = number % 26
    return number_to_letter(number) # Ex. 5 -> E

def letter_to_number(letter : str) -> Optional[int]:
    '''
    Takes a lowercase english letter, and returns a corresponding number 0-25 (a->0, b->1, ... , z->25)
    '''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(0,26):
        if letter == letters[i]:
            return i

def number_to_letter(number : int) -> Optional[str]:
    '''
    Takes a number 0-25, and returns a corresponding lowercase english letter (0->a, 1->b, ... , 25->z)
    '''
    numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(0,26):
        if number == numbers[i]:
            return letters[i]

def is_shiftable_letter(letter : str) -> bool:
    '''
    Returns True if input is a lowercase english letter. Otherwise, returns False.
    '''
    #return letter in 'abcdefghijklmnopqrstuvwxyz'
    #if letter in 'abcdefghijklmnopqrstuvwxyz':
    #    return True
    #else:
    #    return False
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for candidate in letters:
        if letter == candidate:
            return True
    return False

def shift_string(unshifted_text : str, shift_forward : int) -> str:
    '''
    Takes in a string, and outputs a string with each letter shifted forward by 'shift_forward' letters.
    Ex. shifting A forward by 2 gives C

    Punctuation and spaces remain unchanged.
    '''
    new_string = ''
    for letter in unshifted_text:
        if is_shiftable_letter(letter):
            new_string += shift_letter(letter, shift_forward)
        else:
            new_string += letter
    return new_string

def lvl_2():
    lvl2_text = read_file('lvl2.txt')
    characters = set(lvl2_text)
    print((characters))
    for i in characters:
        if is_shiftable_letter(i):
            print(i)
    return characters


def main():
    lvl_0()
    lvl_1()
    lvl_2()
    # print(letter_to_number('z'))
    # print(number_to_letter(25))
    # print(shift_letter('a',2))
    # print(is_shiftable_letter("a"))
    # print(shift_string('abcde', 22))
    # print(shift_string('def/map', 2))
# DO NOT MODIFY BELOW THIS LINE (and don't add other top level stuff)

main()