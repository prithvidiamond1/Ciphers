import argparse

parser=argparse.ArgumentParser(description="Implement 5 ciphers")
group=parser.add_mutually_exclusive_group()

group.add_argument("-c","--caesar",metavar="caesar",type=str,nargs=2,help="\nPerform\
caesar cipher operation on given string.\nUsage: zdciph -c <string> <value to rotate by>")

group.add_argument("-vd","--vigdecr",metavar="vigdecr",type=str,nargs=2,help="\nPerform\
vigenere cipher decryption on given string.\nUsage: zdciph -vd <string to decrypt> <key>")

group.add_argument("-ve","--vigencr",metavar="vigencr",type=str,nargs=2,help="\nPerform\
vigenere cipher encryption on given string.\nUsage: zdciph -ve <string to encrypt> <key>")

group.add_argument("-md","--monodecr",metavar="monodecr",type=str,nargs=1,help="\nPerform\
monoalphabetic cipher decryption on given string.\nUsage: zdciph -md <string to decrypt>")

group.add_argument("-me","--monoencr",metavar="monoencr",type=str,nargs=1,help="\nPerform\
monoalphabetic cipher encryption on given string.\nUsage: zdciph -me <string to encrypt>")

group.add_argument("-rd","--raildecr",metavar="raildecr",type=str,nargs=2,help="\nPerform\
railfence cipher decryption on given string.\nUsage: zdciph -rd <string to decrypt> <key>")

group.add_argument("-re","--railencr",metavar="railencr",type=str,nargs=2,help="\nPerform\
railfence cipher encryption on given string.\nUsage: zdciph -re <string to encrypt> <key>")

group.add_argument("-a","--atbash",metavar="atb",type=str,nargs=1,help="\nPerform\
atbash cipher decryption/encryption on given string.\nUsage: zdciph -a <string to decrypt/encrypt>")

args=parser.parse_args()

def caesar(s,n):
    if not s.isalpha():
        raise
    r=""
    n=int(n)
    for i in s:
        r+=chr((ord(i)+n-65)%26+65) if i.isupper() else chr((ord(i)+n-97)%26+97)  
    return r
  
def vigenere(s,key,vigtype):
    if not (s.isalpha() and key.isalpha()):
        raise

    def keygen(s, key): 
        key=list(key) 
        if len(s)==len(key): 
            return "".join(key)
        else: 
            for i in range(len(s)-len(key)): 
                key.append(key[i%len(key)]) 
        return "".join(key)

    def decrypt(s, key): 
        decr=[] 
        for i in range(len(s)): 
            x=(ord(s[i])-ord(key[i])+26)%26+65
            decr.append(chr(x))
        return "".join(decr) 

    def encrypt(s, key): 
        encr=[] 
        for i in range(len(s)): 
            x=(ord(s[i])+ord(key[i]))%26+65
            encr.append(chr(x))
        return "".join(encr)

    s=s.upper()
    key=keygen(s,key).upper()
    return encrypt(s,key) if vigtype=="e" else decrypt(s,key)

def monoalpha(s,ciphtype):
    if not s.isalpha():
        raise
    s=s.upper()
    key="QWERTYUIOPASDFGHJKLZXCVBNM"
    fin=""
    charsA=[chr(i) for i in range(65,91)]
    charsB=key
    if ciphtype=="d":
        charsA,charsB=charsB,charsA

    for i in s:
        if i in charsA:
            ind=charsA.index(i)
            fin+=charsB[ind]
        else:
            fin+=i
    return fin

def railfence(s,key,railtype):
    if not s.isalpha():
        raise
    def encrypt(text, key):
        rail=[["\n" for i in range(len(text))] for j in range(key)]
        dir_down=False
        row, col=0,0
        
        for i in range(len(text)):
            if row==0 or row==key-1:
                dir_down=not dir_down
            rail[row][col]=text[i]
            col+=1
            row+=1 if dir_down else -1
        result=[]
        for i in range(key):
            for j in range(len(text)):
                if rail[i][j]!="\n":
                    result.append(rail[i][j])
        return "".join(result)

    def decrypt(cipher, key):
        rail=[["\n" for i in range(len(cipher))] for j in range(key)]
        dir_down=None
        row,col=0,0
        for i in range(len(cipher)):
            if row==0:
                dir_down=True
            if row==key-1:
                dir_down=False
            rail[row][col]="*"
            col+=1
            row+=1 if dir_down else -1
        index=0
        for i in range(key):
            for j in range(len(cipher)):
                if rail[i][j]=="*" and index<len(cipher):
                    rail[i][j]=cipher[index]
                    index+=1
        result=[]
        row,col=0,0
        for i in range(len(cipher)):      
            if row==0:
                dir_down=True
            if row==key-1:
                dir_down=False

            if rail[row][col]!="*":
                result.append(rail[row][col])
                col+=1
            row+=1 if dir_down else -1
        return "".join(result)

    key=int(key)
    return encrypt(s,key) if railtype=="e" else decrypt(s,key)

def atbash(s):
    if not s.isalpha():
        raise
    return "".join([chr(155-ord(i)) for i in s.upper()])


try:
    if args.caesar:
        print("{} on rotating by {} = {}".format(*args.caesar,caesar(*args.caesar)))
except ValueError:
    print("Value to rotate by must be an integer")
except:
    print("String cannot contain numbers")

try:
    if args.vigdecr:
        print("{} on decryption using vigenere cipher with key {} = {}".format(*args.vigdecr,vigenere(*args.vigdecr,"d")))
    if args.vigencr:
        print("{} on encryption using vigenere cipher with key {} = {}".format(*args.vigencr,vigenere(*args.vigencr,"e")))
except:
    print("String cannot contain numbers")

try:
    if args.monodecr:
        print("{} on decryption with key QWERTYUIOPASDFGHJKLZXCVBNM = {}".format(*args.monodecr,monoalpha(*args.monodecr,"d")))
    if args.monoencr:
        print("{} on encryption with key QWERTYUIOPASDFGHJKLZXCVBNM = {}".format(*args.monoencr,monoalpha(*args.monoencr,"e")))
except:
    print("String cannot contain numbers")

try:
    if args.raildecr:
        print("{} on railfence decryption with key {} = {}".format(*args.raildecr,railfence(*args.raildecr,"d")))
    if args.railencr:
        print("{} on railfence encryption with key {} = {}".format(*args.railencr,railfence(*args.railencr,"e")))
except ValueError:
    print("Key value must be an integer")
except IndexError:
    print("Key value must be greater than 1")
except:
    print("String cannot contain numbers")

try:
    if args.atbash:
        print("{} on atbash decryption/encryption = {}".format(*args.atbash,atbash(*args.atbash)))
except:
    print("String cannot contain numbers")



