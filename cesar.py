class cesar:
    
    def __init__(self, initkey):
        self.L2I = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ',range(26)))
        self.I2L = dict(zip(range(26),'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        self.key = initkey
    
    def encipher(self, text='SAMPLE'):
        ciphertext = ''
        for c in text.upper():
            if (c.isalpha()):
                ciphertext += self.I2L[
                    (self.L2I[c] + self.key) % 26]
            else:
                ciphertext += c
        return ciphertext

    def decipher(self, text='VDPSOH'):
        ciphertext = ''
        for c in text.upper():
            if(c.isalpha()): 
               ciphertext += self.I2L[
                    (self.L2I[c] - self.key) % 26]
            else: 
               ciphertext += c
        return ciphertext
    

if (__name__ == '__main__'):
    cipher = cesar(3)
    print(cipher.encipher('SAMPLE'))
    print(cipher.decipher(cipher.encipher('SAMPLE')))
