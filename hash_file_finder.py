import os
import string
import hashlib

EVIDENCE_FILES = {}
class Sum:
    def calculate(self,path):
        try:
            md5_hash = hashlib.md5(open(path,'rb').read()).hexdigest()
            return md5_hash
        except:
            return "invalid_file"

class Drives:
    def list(self):
        available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
        
        option = 0
        print("0 All")
        for drive in available_drives:
            print(str(option)+" "+drive)
            option = option+1
        drive_letter = input("Choose Drive letter to search > ")
        if(drive_letter == '0'):
            print("All drives Selected for scan")
            return available_drives
        else:
            drive_s = []
            print(str(available_drives[int(drive_letter)])+" Selected for scan")
            drive_s.append(available_drives[int(drive_letter)])
            return drive_s

class File:
    def get_files(self,drive_letter,evidence_sum):
        SUM = Sum()
        print("\n")
        print("_"*100)
        print("\n")
        for path, subdirs, files in os.walk(drive_letter):
            for name in files:
                file_path= os.path.join(path, name)
                hash_sum = SUM.calculate(file_path)
                if hash_sum in evidence_sum:
                    evidence_file = EVIDENCE_FILES[hash_sum]
                    print("[+][File Path : "+file_path+"][Hash matched][Hash : "+hash_sum+"][Evidence : "+evidence_file+"]")
        print("\n")
        print("_"*100)
    def evidence_file(self,evidence):
        SUM = Sum()
        evidence_hash = []
        for path, subdirs, files in os.walk(evidence):
            for name in files:
                file_path= os.path.join(path, name)
                hash_string = SUM.calculate(file_path)
                EVIDENCE_FILES[hash_string] = file_path
                evidence_hash.append(hash_string)
        return evidence_hash 

DRIVERS = Drives()
FILES = File()
class Main:
    def start(self):
        try:
            drive_list = DRIVERS.list()
            evidence = input("Enter evidence files Folder > ")
            evidence_sum = FILES.evidence_file(evidence)
            for letter in drive_list:
                FILES.get_files(letter,evidence_sum)
            continue_menu = input("Do you want to continue (Y/N)")
            if(continue_menu == "Y" or continue_menu == "y"):
                MAIN = Main()
                MAIN.start()
            else:
                print("Exiting..")
        except:
            print("Error Occured")
            continue_menu = input("Do you want to continue (Y/N)")
            if(continue_menu == "Y" or continue_menu == "y"):
                MAIN = Main()
                MAIN.start()
LABEL = """


░░░██╗░██╗░░░░░░░████████╗██████╗░░█████╗░░█████╗░██╗░░██╗
██████████╗░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
╚═██╔═██╔═╝█████╗░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░
██████████╗╚════╝░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░
╚██╔═██╔══╝░░░░░░░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗
░╚═╝░╚═╝░░░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝


"""
print(LABEL)
MAIN = Main()
MAIN.start()
