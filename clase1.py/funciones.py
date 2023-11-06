def suma(num):
    print(num, end = "+")
    if num == 1:
       return 1 + "="
    else:
       return num + suma (num -1)
def factorial (num):
   if num == 1:
      return 1 
   else:
      return num * factorial (num -1 )
    
if __name__=='__main__':
  print(suma(10))







