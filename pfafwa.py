def letter_to_int(character):

    if(character.isupper() == True):

        number = ord(character) - 64

    else:    number = ord(character) - 96
   
    return number


print(letter_to_int('z'))


def word_to_int(text):

    text1 = ""

    number_list = []

    for x in text:

       text1 = str(letter_to_int(x))

       text2 = int(text1)

       number_list.append(text2)
 
    return number_list


print(word_to_int("abc"))


def get_letter(number):
    
    if(number >= 0 and number <= 26):

        letter = chr(number+96)


    return letter


print(get_letter(1))


def list_to_word(numbers):

    s = ""

    for item in numbers:

        s+= get_letter(item)

    return s


print(list_to_word(word_to_int("abc")))


def caesar_encrypt(message, key):

    number =  word_to_int(message)

    shift = [x+key for x in number]

    cipher= list_to_word(shift)
  
    return cipher
    

print(caesar_encrypt("ryan", 1))
