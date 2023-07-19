from browser_history import get_history
import subprocess
import wmi

class Save:
    def extracted_data(self,history,file_name):
        with open(file_name, "a") as file:
            file.write("\n" + history)

class Data:
    def __init__(self) -> None:
        save_obj = Save()
        self.save = save_obj
    
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

class Menu:
    def data(self):
        menu_functions = ["browser_history","installed_apps","running_applications"]
        menu_labels = ["browser history","Installed Apps","Running Apps"]
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
