## This project allows you to encypt and decrypt a message via 5 different ciphers.

    Ciphers available: 
    1. Caesar cipher
    2. Vigenere cipher
    3. Monoalphabetic cipher
    4. Railfence cipher
    5. Atbash cipher

## Usage:

    $ git clone https://github.com/Omicron02/Ciphers
    $ cd Ciphers/executables
    
    **To run the executable on Linux, use ./zdciph <args> and to run it on Windows,
    use zdciph <args>**

    Format for every cipher:

    Caesar:
    $ ./zdciph -c[or --caesar] <word to rotate> <number to rotate by>

    Vigenere:
    $ ./zdciph -ve[or --vigencr] <word to encrypt> <encryption key word>
    $ ./zdciph -vd[or --vigdecr] <word to decrypt> <decryption key word>

    Monoalphabetic:
    $ ./zdciph -me[or --monoencr] <word to encrypt>
    $ ./zdciph -md[or --monodecr] <word to decrypt>

    Railfence:
    $ ./zdciph -re[or --railencr] <word to encrypt> <integer encryption key>
    $ ./zdciph -rd[or --raildecr] <word to decrypt> <integer decryption key>

    Atbash:
    $ ./zdciph -a[or --atbash] <word to decrypt/encrypt>



