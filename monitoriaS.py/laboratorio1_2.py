def check(cardN, paswrd):
    for i in cards:
        if i[0] == cardN:
            if i[1] == paswrd:
                return True
            else:
             print("Invalid key")
            break
        else:
            print("Invalid card")
            break


def whithdrawal(cardN, amount):
    for i in cards:
        if i[0] == cardN:
            if i[2] >= 10000:
                i[2] = i[2] - amount
                print(f"you have withdrawn: {amount}")
                print(f"remaining balance: {i[2]}")
                return True
            else:
                print("Clave invalida")


if __name__=='__main__':
    global cards
    cards = [[567890, 1234, 10000], [789012, 5678, 5000],[345678, 9012, 20000]]

    cardN = int(input("enter you card: "))
    clue = int(input("enter you password: "))

    if check (cardN, clue) == True:
        amount = int(input("¿how much do you want to withdraw?: "))
        print(whithdrawal(cardN, amount))









