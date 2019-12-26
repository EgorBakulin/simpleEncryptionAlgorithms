class vijener:
    
    def __init__(self, initkey):
        self.L2I = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ',range(26)))
        self.I2L = dict(zip(range(26),'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        self.key = []
        for leter in initkey:
            self.key.append(self.L2I[leter]) 
        
    def encipher(self, text):
        ciphertext = ''
        keyindex = 0
        for c in text.upper():
            if (c.isalpha()):
                ciphertext += self.I2L[
                    (self.L2I[c] + self.key[keyindex]) % 26]
            else:
                ciphertext += c
            keyindex += 1
            keyindex = keyindex % len(self.key)
        return ciphertext
    
    def decipher(self, text):
        ciphertext = '' 
        keyindex = 0
        for c in text.upper():
            if(c.isalpha()): 
               ciphertext += self.I2L[
                    (self.L2I[c] - self.key[keyindex]) % 26 ]
            else: 
               ciphertext += c
            keyindex += 1
            keyindex = keyindex % len(self.key)
        return ciphertext


if (__name__ == '__main__'):
    cipher = vijener('KEY')
    print(cipher.encipher('SAMPLE'))
    print(cipher.decipher(cipher.encipher('SAMPLE')))
