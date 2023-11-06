def collatz (num):
    print(int(num))
    if num == 1:
        return 1
    elif num %2 == 0:
        return collatz (num/2)
    else:
        return collatz(num*3+1)
    
print(collatz(10))



__name__=='__main__'

