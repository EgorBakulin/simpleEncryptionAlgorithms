import cesar
import transposition
import vijener

print('Select your favorite cipher.'
      + '\n1. cesar'
      + '\n2. transposition'
      + '\n3. vijener'
      + '\n4. playfer(comming soon)'
      + '\n0. exit')

chose = int(input())
if(chose == 1):
    print('You selected cesar crypt'
          + '\nPlease enter your key.')
    key = int(input())
    cipher = cesar.cesar(key)
    
elif(chose == 2):
    print('You selected vijener crypt'
          + '\nPlease enter your key.'
          + '\nThe length must be equal to the'
          + '\nlength of the encrypted word.')
    key = input()
    cipher = transposition.transposition(key)

elif(chose == 3):
    print('You selected vijener crypt'
          + '\nPlease enter your key.'
          + '\nSeparate numbers with spaces')
    key = input()
    cipher = vijener.vijener(key)

elif(chose == 4):
    pass

elif(chose == 0):
    print('press Enter to exit...')
    input()
    exit()

else:
    print('Wrong chose')
    print('press Enter to exit...')
    input()
    exit()
    

print('1. Encrypt text'
      + '\n2. Decrypt text')

chose = int(input())
print('input text')
text = input()
if(chose == 1):
    text = cipher.encipher(text)

if(chose == 2):
    text = cipher.decipher(text)

print(text)
