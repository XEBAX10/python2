# deborador de vocales

def get_word():
    user_word=input("enter word:")
    return user_word.upper()

#condicion
def devour_vowels(word):
    for letter in word:
        if letter in "A":
            continue
        elif letter in "E":
            continue
        elif letter in "I":
            continue
        elif letter in "O":
            continue
        elif letter in "U":
            continue
        print(letter)

def outgoing_data():
    word = get_word()
    devour_vowels (word)

if __name__=='__main__':
    outgoing_data()

    


















