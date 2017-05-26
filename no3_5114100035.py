from operator import xor
from pip._vendor.distlib.compat import raw_input


firsttext = raw_input("masukkan plaintext: ")

TextArray = [None] * len(firsttext)

def encrypt(plaintext,Key):
   
   #membuat string ke bentuk ascii
    asciikey = [None] * len(Key)
    for i in range(0,len(Key)):
        asciikey[i] = ord(Key[i])
        
	#membagi key ke2 bagian
    k0 = [None] * 4
    k1 = [None] * 4
    j = 0
    for i in range(0,len(asciikey)):
        if i <= 3:
            k0[i] = asciikey[i]
        else:
            k1[j] = asciikey[i]
            j = j + 1

			
    recur = len(plaintext)/4
    null = 4 - (len(plaintext)%4)
    if null > 0:
        recur = recur + 1

    asciitext = [None] * (recur*4)
    for i in range(0,len(asciitext)):
        if i < len(plaintext):
            asciitext[i] = ord(plaintext[i])
        else:
            asciitext[i] = ord(' ');

    diisi = (recur*4)
	
	#di xor
    x = 0
    for i in range(0,recur):
        for j in range(0,4):
            asciitext[x] = xor(asciitext[x], k0[j])
            x = x + 1

    #print asciitext
    #print k1
    x = 0
    EncryptedText = [None] * len(asciitext)
    for i in range(0,recur):
        for j in range(0,4):
            EncryptedText[x] = asciitext[x] + k1[j]
            #EncryptedText[x] = EncryptedText%256
            #print EncryptedText[x]
            x = x + 1

    hasilEncrypted = [None] * (len(EncryptedText) - null)
    for i in range(0,len(hasilEncrypted)):
        hasilEncrypted[i] = chr(EncryptedText[i])

    return hasilEncrypted


def decrypt(hasilEnkripsi, Key):
    
    asciikey = [None] * len(Key)
    for i in range(0, len(Key)):
        asciikey[i] = ord(Key[i])

    k0 = [None] * 4
    k1 = [None] * 4

    j = 0
    for i in range(0, len(asciikey)):
        if i <= 3:
            k0[i] = asciikey[i]
        else:
            k1[j] = asciikey[i]
            j = j + 1

    recur = len(hasilEnkripsi) / 4
    sisa = len(hasilEnkripsi) % 4
    ukuranEncryp = ((4*recur) + sisa)
    asciiEncryp = [None] * ukuranEncryp
    for i in range(0, len(asciiEncryp)):
        asciiEncryp[i] = ord(hasilEnkripsi[i])

    
    for i in range(0,ukuranEncryp):
        asciiEncryp[i] = asciiEncryp[i] - k1[i%4]

   

    hasilDecryp = [None] * len(asciiEncryp)
    for i in range(0,ukuranEncryp):
        hasilDecryp[i] = xor(asciiEncryp[i],k0[i%4])

    hasilDecrypted = [None] * len(hasilDecryp)
    for i in range(0,len(hasilDecrypted)):
        hasilDecrypted[i] = chr(hasilDecryp[i])

    return hasilDecrypted

key = raw_input('masukkan key(8 huruf)')

for i in range(0,len(firsttext)):
    TextArray[i] = firsttext[i]


value1 = encrypt(TextArray,key)
print "enkripsi dari " + firsttext + ":" + str(value1)

value2 = decrypt(value1,key)
print "dekripsi dari" + str(value1) + ":" + str(value2)