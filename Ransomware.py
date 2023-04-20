import pyAesCrypt
import os

class Protect:
    
    def encrypt(self,password,file,output_file):
        pyAesCrypt.encryptFile(file, output_file, password)
    
    def decrypt(self,password,file,output_file):
        pyAesCrypt.decryptFile(file, output_file, password)

class File:
    def list_files(self,drive_letter):
        for path, subdirs, files in os.walk(drive_letter):
            for name in files:
                print(os.path.join(path, name))
                
file_obj = File()
file_obj.list_files('F:/')
