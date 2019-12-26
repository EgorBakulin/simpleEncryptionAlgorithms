class transposition:

    def __init__(self,initkey):
        self.key = []
        for leter in initkey.split():
            self.key.append(int(leter)) 
        print(self.key)

    def encipher(self, text):
        if(len(self.key) != len(text)):
            print('enchiper error')
            return None
        output = ''
        for number in self.key: 
            output = output + text[number]
        return output
    
    def decipher(self, text):
        if(len(self.key) != len(text)):
            print('enchiper error')
            return 0
        output = ''
        for number in self.key: 
            output = output + text[self.key.index(len(output))]
        return output

if (__name__ == '__main__'):
    cipher = transposition('1 2 0 5 3 4')
    print(cipher.encipher('SAMPLE'))
    print(cipher.decipher(cipher.encipher('SAMPLE')))
