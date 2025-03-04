def lvl_1 ():
    ans_1 = 2**38
    return ans_1

def read_file(text_file_name):
    text_file = open(text_file_name, "r")
    contents = text_file.read()
    text_file.close()A
    return contents

def lvl_2 ():
    cryptic_string = read_file("lvl2.txt")
    print(cryptic_string)
    #ans_2 =

def main():
    print(lvl_1())

    lvl_2()

# DO NOT MODIFY BELOW THIS LINE (and don't add other top level stuff)

main()