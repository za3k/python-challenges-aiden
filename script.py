from typing import Optional


def lvl_1 ():
    ans_1 = 2**38
    return ans_1

def read_file(text_file_name: str) -> str:
    text_file = open(text_file_name, "r")
    contents = text_file.read()
    text_file.close()
    return contents

def lvl_2 ():
    cryptic_string = read_file("lvl2.txt")
    print(cryptic_string)

    #ans_2 =

def shift_string(unshifted_text : str, shift_forward : int) -> str:
    """
    Shift letters in the text forward (A->B) by `shift_forward` letters
    """

    return "TEST SHIFT"

def shift_letter (letter : str , shift_forward : int) -> str:
    return 'x'

def letter_to_number(letter : str) -> Optional[int]:
    if letter == "a": return 1
    elif letter == "b": return 2
    elif letter == "c": return 3
    elif letter == "d": return 4
    elif letter == "e": return 5
    elif letter == "f": return 6
    elif letter == "g": return 7
    elif letter == "h": return 8
    elif letter == "i": return 9
    elif letter == "j": return 10
    elif letter == "k": return 11
    elif letter == "l": return 12
    elif letter == "m": return 13
    elif letter == "n": return 14
    elif letter == "o": return 15
    elif letter == "p": return 16
    elif letter == "q": return 17
    elif letter == "r": return 18
    elif letter == "s": return 19
    elif letter == "t": return 20
    elif letter == "u": return 21
    elif letter == "v": return 22
    elif letter == "w": return 23
    elif letter == "x": return 24
    elif letter == "y": return 25
    elif letter == "z": return 26
    else:
        return None

#def number_to_letter
#def is_shiftable_letter

def main():
    print(lvl_1())

    lvl_2()

    print(shift_string("AAAAA", 5))
    print(shift_letter('f', 6))
    print(letter_to_number("u"))
# DO NOT MODIFY BELOW THIS LINE (and don't add other top level stuff)

main()