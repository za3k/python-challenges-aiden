from typing import Optional
import re

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
    #print(f'lvl 1 decoded hint: {new_string}')
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
    return letter.islower()

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
    #print((characters))
    #for i in characters:
        #if is_shiftable_letter(i):
            #print(i)
    print('lvl 2 solution: http://www.pythonchallenge.com/pc/def/equality.html')

def lvl_3():
    lvl3_text = read_file('lvl3.txt')
    ans3 = ''
    # Regex version
    #pattern = '[a-z][A-Z][A-Z][A-Z]([a-z])[A-Z][A-Z][A-Z][a-z]'
    #for m in re.finditer(pattern, lvl3_text):
    #    ans3 += m[1]
    for index in range(4, len(lvl3_text)-4):
        left_character = lvl3_text[index - 1]
        right_character = lvl3_text[index + 1]
        left_left_character = lvl3_text[index - 2]
        right_right_character = lvl3_text[index + 2]
        left_left_left_character = lvl3_text[index - 3]
        right_right_right_character = lvl3_text[index + 3]
        left_left_left_left_character = lvl3_text[index - 4]
        right_right_right_right_character = lvl3_text[index + 4]
        character = lvl3_text[index]
        if (character.islower()
            and left_character.isupper()
            and right_character.isupper()
            and left_left_character.isupper()
            and right_right_character.isupper()
            and left_left_left_character.isupper()
            and right_right_right_character.isupper()
            and left_left_left_left_character.islower()
            and right_right_right_right_character.islower()):
            ans3 += character
    print(f'lvl 3 solution: http://www.pythonchallenge.com/pc/def/{ans3}.php')

def cached_get(url, dbpath="linkedlist.db"):
    """Returns the text at a URL (uses an on-disk cache)"""
    import requests
    import shelve
    with shelve.open(dbpath) as db:
        if url not in db:
            r = requests.get(url)
            db[url] = r.text
        return db[url]

def get_number(text: str) -> int:
    '''
    Take the text of a lvl3 puzzle, ex: "and the next nothing is 44827"
    returns 44827
    '''
    numbers = int(text[-5:])
    return numbers

def next_url_is(numbers: int) -> str:
    return f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={numbers}'

def lvl_4():
    #next_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
    next_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022'
    while True:
        text = cached_get(next_url)
        numbers = get_number(text)
        next_url = next_url_is(numbers)
        print(next_url)


def main():
    lvl_0()
    lvl_1()
    lvl_2()
    lvl_3()
    print(get_number('and the next nothing is 44827'))
    print(get_number('and the next nothing is 559'))
    lvl_4()
    # print(letter_to_number('z'))
    # print(number_to_letter(25))
    # print(shift_letter('a',2))
    # print(is_shiftable_letter("a"))
    # print(shift_string('abcde', 22))
    # print(shift_string('def/map', 2))
# DO NOT MODIFY BELOW THIS LINE (and don't add other top level stuff)

main()