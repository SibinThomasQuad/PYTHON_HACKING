from browser_history import get_history
import subprocess
import wmi
import hashlib
import os
import exifread

class Save:
    def extracted_data(self,history,file_name):
        with open(file_name, "a") as file:
            file.write("\n" + history)

class Data:
    def __init__(self) -> None:
        save_obj = Save()
        self.save = save_obj
    
    def get_files_in_subfolders(self,drive_path):
        file_list = []
        for root, _, files in os.walk(drive_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                file_list.append(file_path)

        return file_list
    
    def get_files(self):
        drive_path = input("Enter the drive path (e.g., C:/ or D:/): ")
        if not os.path.exists(drive_path):
            print("Drive not found.")
        else:
            all_files = self.get_files_in_subfolders(drive_path)

            print("All files in subfolders:")
            for file_path in all_files:
                self.save.extracted_data(file_path,"file_structure.dump")
            
    def running_applications(self):
        f = wmi.WMI()
        self.save.extracted_data("pid   Process name","running_apps.dump")
        for process in f.Win32_Process():
            running_app = str(f"{process.ProcessId:<10} {process.Name}")
            self.save.extracted_data(running_app,"running_apps.dump")
    
    def installed_apps(self):
        Data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
        a = str(Data)
        try:
            for i in range(len(a)):
                software_name = a.split("\\r\\r\\n")[6:][i]
                self.save.extracted_data(software_name,"installed_apps.dump")

        except IndexError as e:
            print("All Done")
    
    def browser_history(self):
        try:
            outputs = get_history()
            historys = outputs.histories
            for history in historys:
                history_dump = str(history[0])+"  "+str(history[1])
                self.save.extracted_data(history_dump,"browser_history.dump")
            print("[+] browser history dumping success!")
        except:
            print("[-] browser history dumping failed")
    
    def calculate_md5(self,file_path=0):
        if file_path == 0:
            file_path = input("Input file path > ")
        md5_hash = hashlib.md5()
        with open(file_path, "rb") as file:
            # Read the file in chunks to handle large files efficiently
            for chunk in iter(lambda: file.read(4096), b""):
                md5_hash.update(chunk)
        hash_value = md5_hash.hexdigest()
        print("[+] file "+file_path)
        print("[+] MD5 Hash : "+hash_value)
    
    def calculate_sha1(self,file_path=0):
        if file_path == 0:
            file_path = input("Input file path > ")
        sha1_hash = hashlib.sha1()
        with open(file_path, "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                sha1_hash.update(chunk)
        hash_value = sha1_hash.hexdigest()
        print("[+] file "+file_path)
        print("[+] SHA1 Hash : "+hash_value)
    
    def extract_metadata(self):
        file_path = input("Enter file path > ")
        with open(file_path, "rb") as file:
            tags = exifread.process_file(file)
        return tags

class Menu: 
    def data(self):
        menu_functions = ["browser_history","installed_apps","running_applications","calculate_md5","calculate_sha1","get_files","extract_metadata"]
        menu_labels = ["browser history","Installed Apps","Running Apps","MD5 Hash File","SHA1 Hash File","Get file structure","Meta data"]
        menu_info = {"functions":menu_functions,"lables_name":menu_labels}
        return menu_info

    def menu_prompts(self):
        menu_infomartion = self.data()
        menu_labels = menu_infomartion["lables_name"]
        menu_index = 0
        for menu in menu_labels:
            print(str(menu_index)+"-"+menu)
            menu_index = menu_index + 1
    
    def choosed_menu(self,menu_index):
        data = Data()
        menu_functions = self.data()["functions"]
        function_name = menu_functions[menu_index]
        if hasattr(data, function_name) and callable(getattr(data, function_name)):
            function = getattr(data, function_name)
            function()
        
class Input:
    def choose_menu(self):
        menu_id = input("Choose your option > ")
        return int(menu_id)

class Main:
    def __init__(self) -> None:
        menu_obj = Menu()
        input_obj = Input()
        self.input = input_obj
        self.menu = menu_obj
    
    def start(self):
        self.menu.menu_prompts()
        menu_index = self.input.choose_menu()
        self.menu.choosed_menu(menu_index)

main = Main()
main.start()
