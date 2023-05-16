import random
import string
import datetime
import hashlib
import os
import psutil

class Drive:
    def list(self):
        drives = [ chr(x) + ":" for x in range(65,91) if os.path.exists(chr(x) + ":") ]
        return drives
    
    def get_size(self,drive_letter):
        drive = psutil.disk_usage(drive_letter + '/')
        size_in_mb = drive.total / (1024 * 1024)
        return size_in_mb
        
    
class File:
    def generate_file_name(self):
        now = datetime.datetime.now()
        milliseconds = now.microsecond // 1000  # Convert microseconds to milliseconds
        # Format the datetime string
        datetime_string = now.strftime("%Y-%m-%d %H:%M:%S") + f".{milliseconds:03d}"
        file_name = hashlib.md5(datetime_string.encode()).hexdigest()
        return file_name
    
    def generate_one_mb_text_file(self,file_path):
        file_size = 1024 * 1024  # 1MB
        with open(file_path, 'w') as file:
            while file.tell() < file_size:
                text = ''.join(random.choices(string.ascii_letters + string.digits, k=1024))
                file.write(text)
        
        print(f"Generated file: {file_path}")

def main():
    drive_obj = Drive()
    file_obj = File()
    drive_letters = drive_obj.list()
    index = 0
    for drive_letter in drive_letters:
        print(str(index)+","+str(drive_letter))
        index = index + 1
    
    option = input("Choose the drive > ")
    drive_choosen = drive_letters[int(option)]
    drive_size = drive_obj.get_size(str(drive_choosen))
    print("[+] You choosed "+str(drive_choosen)+" to permenent eraze")
    print("[+] Size "+str(drive_size))
    #print(file_obj.generate_file_name())

main()
