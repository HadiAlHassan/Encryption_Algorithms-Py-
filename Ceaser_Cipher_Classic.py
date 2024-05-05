#Ceaser Cipher-----------------Classical Key Equal 3-----------------------------
def Encrypt_Ceaser(s):
    st = ""
    for i in s:
        if i == " ":
            st += i
            
        elif i.isupper():
          st +=  chr((ord(i) + 3 -65) % 26 + 65)
        else:
            st += chr((ord(i) + 3 - 97) % 26 + 97)
            
    return st

def Decrypt_Ceaser(s):
    st = ""
    for i in s:
        if i == " ":
            st += i
        elif i.isupper():
            st += chr((ord(i) - 3 - 65) % 26 + 65)
        else:
            st += chr((ord(i) - 3 - 97) % 26 + 97)
            
    return st


PlainText = input()

Encrypted_Message = Encrypt_Ceaser(PlainText)
print(Encrypted_Message)
Message = Decrypt_Ceaser(Encrypted_Message)
print(Message)