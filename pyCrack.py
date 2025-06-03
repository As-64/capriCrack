import hashlib
import os
import sys
import pyfiglet
from easygui import *

print("*******************************************************")
print(pyfiglet.figlet_format("capriCrack"))
print("""

capriCrack 1.0.0
Created by Alfie Skidmore, owner of CapricornCyberServicesUKX
A hash cracking tool with a graphical user interface
alfieskidmorecuk@outlook.com
*******************************************************""")

def identify_type(hashed):
    types = {
        32:"MD5",
        40:"SHA-1",
        64:"SHA-256"
        }
    hash_length = len(hashed)
    if hash_length in types:
        print(f"[+] Hash likely to be of type {types[hash_length]} [+]")
        return types[hash_length]
    else:
        print("[-] Hash not identified [-]")
        sys.exit(0)

def load_wordlist():
    choices=[x for x in os.listdir("wordlists")]
    choices.append("Exit program")
    wordlist = choicebox("Select which wordlist you would like to use: ","Wordlist selection",choices=choices)
    if not wordlist or wordlist == "Exit program":
        sys.exit(0)
    print(f"[+] Wordlist '{wordlist}' loaded [+]")
    return wordlist

def crack_hash(hash_type, wordlist, hashed):
    if hash_type == "Don't know":
        hash_type = identify_type(hashed)
        if not hash_type:
            sys.exit(0)
    
    with open(wordlist,"rb") as file:
        for line in file.read().splitlines():
            match hash_type:
                case "MD5":
                    line_hash = hashlib.md5(line)
                case "SHA-1":
                    line_hash = hashlib.sha1(line)
                case "SHA-256":
                    line_hash = hashlib.sha256(line)
                        

            hashed_line = line_hash.hexdigest()
            if hashed_line == hashed:
                print(f"[+] Found cleartext password: {line.decode()} [+]")
                sys.exit(0)
                    
                        
    
    print("No password found")

hashed = enterbox("Please enter the hashed value","Hash entry")
print(f"[+] Hashed value '{hashed}' loaded [+]") if hashed != None else sys.exit(0)
hash_type = choicebox("Please select the hash type of the hash we will be cracking: ","Select hash type",choices=["MD5","SHA-1","SHA-256","Don't know"])
if hash_type == None:
    sys.exit(0)
else:
    print(f"[+] Hash type '{hash_type}' loaded [+]") if hash_type != "Don't know" else print("[-] Attempt to identify hash will be made [-]")
wordlist = load_wordlist()
crack_hash(hash_type, wordlist, hashed)
