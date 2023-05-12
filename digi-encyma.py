import os
import pyAesCrypt
import shutil
from getpass import getpass
import cryptocode


BANNER = '''


██████╗░██╗░██████╗░██╗░░░░░░███████╗███╗░░██╗░██████╗░██╗███╗░░░███╗░█████╗░
██╔══██╗██║██╔════╝░██║░░░░░░██╔════╝████╗░██║██╔════╝░██║████╗░████║██╔══██╗
██║░░██║██║██║░░██╗░██║█████╗█████╗░░██╔██╗██║██║░░██╗░██║██╔████╔██║███████║
██║░░██║██║██║░░╚██╗██║╚════╝██╔══╝░░██║╚████║██║░░╚██╗██║██║╚██╔╝██║██╔══██║
██████╔╝██║╚██████╔╝██║░░░░░░███████╗██║░╚███║╚██████╔╝██║██║░╚═╝░██║██║░░██║
╚═════╝░╚═╝░╚═════╝░╚═╝░░░░░░╚══════╝╚═╝░░╚══╝░╚═════╝░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝

'''

STRING_CYPHER = ''
ENCRYPTED_STRING = ''

class Assets:
    line = "_"*100
    start = " "*5
    

class Protect:
    
    def encrypt(self,password,file,output_file):
        pyAesCrypt.encryptFile(file, output_file, password)
    
    def decrypt(self,password,file,output_file):
        pyAesCrypt.decryptFile(file, output_file, password)
    
    def encrypt_text(self,password):
        global STRING_CYPHER
        encoded = cryptocode.encrypt(STRING_CYPHER,password)
        STRING_CYPHER = encoded
    
    def decrypt_text(self,password):
        global ENCRYPTED_STRING
        decoded = cryptocode.decrypt(ENCRYPTED_STRING, password)
        ENCRYPTED_STRING = decoded
        
class Drive:
    def list(self):
        drives = [ chr(x) + ":" for x in range(65,91) if os.path.exists(chr(x) + ":") ]
        return drives
        
class File:
    
    def replace_file(self,original_file,encrypted_file):
        shutil.copyfile(encrypted_file, original_file)

class View:
    
    def __init__(self) -> None:
        self.drive_obj = Drive()
        self.file_ob = File()
        self.protect_obj = Protect()
        
    def banner(self):
        print(Assets.line)
        print("\n")
        print("\n")
        print(BANNER)
        print(Assets.start+"TOOL TO PROTECT YOUR DRIVES AND FILES")
        print("\n")  
    
    def string_encrypt_option(self):
        global STRING_CYPHER
        string = input(Assets.start+("Enter the string to encrypt\n"+Assets.start))
        rounds = input(Assets.start+"Enter the round you want to encrypt : ")
        password = getpass(Assets.start+"Enter the password to encrypt : ")
        STRING_CYPHER = string
        for round in range(int(rounds)):
            self.protect_obj.encrypt_text(password)
        print(Assets.line)
        print(Assets.start+"Encrypted string is")
        print("\n")
        print(Assets.start+STRING_CYPHER)
        print("\n")
        
    def string_decrypt_option(self):
        global ENCRYPTED_STRING
        string = input(Assets.start+("Enter the string to decrypt\n"+Assets.start))
        rounds = input(Assets.start+"Enter the round that you used to encrypt : ")
        password = getpass(Assets.start+"Enter the password to decrypt : ")
        ENCRYPTED_STRING = string
        for round in range(int(rounds)):
            self.protect_obj.decrypt_text(password)
        print(Assets.line)
        print(Assets.start+"decrypted string is")
        print("\n")
        print(Assets.start+ENCRYPTED_STRING)
        print("\n")
        
    def decrypt_option(self,drives):
        print("\n")
        option_input = input(Assets.start+"Choose the drive that you want to decrypt : ")
        drive_to_decrypt = drives[int(option_input)]
        print(Assets.start+"You selected "+str(drive_to_decrypt)+" to decrypt")
        print(Assets.line)
        print("\n")
        rounds = input(Assets.start+"Enter the round that you used to encrypt : ")
        password = getpass(Assets.start+"Enter the password to decrypt : ")
        print(Assets.line)
        print("\n")
        print(Assets.start+"DECRYPTION STARTED")
        print("\n")
        for path, subdirs, files in os.walk(drive_to_decrypt):
            for name in files:
                
                for round in range(int(rounds)):
                    file_to_decrypt = os.path.join(path, name)
                    print("\n")
                    print(Assets.start+"[*] Decrypting file "+file_to_decrypt+"[ROUND "+str(round+1)+"]")
                    try:
                        file_after_decrypt = file_to_decrypt+".DECRYPTING"
                        self.protect_obj.decrypt(password,file_to_decrypt,file_after_decrypt)
                        self.file_ob.replace_file(file_to_decrypt,file_after_decrypt)
                        os.remove(file_after_decrypt)
                        print(Assets.start+"[+] File "+file_to_decrypt+" is decrypted successfully [ROUND "+str(round+1)+"]")
                    except:
                        print(Assets.start+"[-] File "+file_to_decrypt+" is decryption failed [ROUND "+str(round+1)+"]")
                        
        print(Assets.start+"DECRYPTION COMPLETED")     
    
    def encrypt_option(self,drives):
        print("\n")
        option_input = input(Assets.start+"Choose the drive that you want to encrypt : ")  
        drive_to_encrypt = drives[int(option_input)]
        print(Assets.start+"You selected "+str(drive_to_encrypt)+" to encrypt")
        print(Assets.line)
        print("\n")
        rounds = input(Assets.start+"Enter the round you want to encrypt : ")
        password = getpass(Assets.start+"Enter the password to encrypt : ")
        print(password)
        print(Assets.line)
        print("\n")
        print(Assets.start+"ENCRYPTION STARTED")
        print("\n")
        protect_obj = Protect()
        for path, subdirs, files in os.walk(drive_to_encrypt):
            for name in files:
                for round in range(int(rounds)):
                    file_to_encrypt = os.path.join(path, name)
                    print("\n")
                    print(Assets.start+"[*] Encrypting file "+file_to_encrypt+"[ROUND "+str(round+1)+"]")
                    try:
                        file_after_encrypt = file_to_encrypt+".ENCRYPTING"
                        self.protect_obj.encrypt(password,file_to_encrypt,file_after_encrypt)
                        self.file_ob.replace_file(file_to_encrypt,file_after_encrypt)
                        os.remove(file_after_encrypt)
                        print(Assets.start+"[+] File "+file_to_encrypt+" is ecrypted successfully [ROUND "+str(round+1)+"]")
                    except:
                        print(Assets.start+"[-] File "+file_to_encrypt+" is encryption failed [ROUND "+str(round+1)+"]")
        print("\n")
        print(Assets.start+"ENCRYPTION COMPLETED")
        print("\n")

    def process_options(self):
        print(Assets.line)
        print("\n")
        print(Assets.start+"0, Encrypt Drive")
        print(Assets.start+"1, Decrypt Drive")
        print(Assets.start+"2, Encrypt Text")
        print(Assets.start+"3, Decrypt Text")
        print(Assets.start+"99, Quit")
        print("\n")
        mode = int(input(Assets.start+"Select The option : "))
        if(mode == 99):
            quit()
        drives = self.drive_obj.list()
        print(Assets.line)
        print("\n")
        if(mode == 0 or mode == 1):
            for drive in drives:
                drive_name = drive
                drive_number = drives.index(drive)
                print(Assets.start+str(drive_number)+","+str(drive_name))
        if(mode == 0):
            self.encrypt_option(drives)
        if(mode == 1):
            self.decrypt_option(drives)
        if(mode == 2):
            self.string_encrypt_option()
        if(mode == 3):
            self.string_decrypt_option()
            
def main():           
    try:
        view_obj = View()
        view_obj.banner()
        view_obj.process_options()
        continue_option = input(Assets.start+"Do you want to continue (y/n)")
        if(continue_option == 'y'):
            os.system('cls')
            main()
        else:
            quit
    except:
        print("\n[*****] EXITING APPLICATION..")

main()
