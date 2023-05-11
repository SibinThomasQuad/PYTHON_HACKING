from browser_history import get_history
import datetime
import csv
import random

TIME = datetime.datetime.now()
NUM  = num = random.random()
FILE_NAME = "browser_history"+str(NUM)+".csv"

class Store:
    
    def save_csv(self,data):
        filename = FILE_NAME
        fields = ['Time', 'URL']
        with open(filename, 'w') as csvfile: 
            csvwriter = csv.writer(csvfile) 
            csvwriter.writerow(fields) 
            csvwriter.writerows(data)

class Data:
    
    def browsing_history(self):
        try:
            storage_obj = Store()
            print("\n") 
            print("[+] Browser history export started")
            print("\n") 
            full_data = []
            file_name = "Broser_history.txt"
            outputs = get_history()
            his = outputs.histories
            for history in his:
                browse_data = []
                time = history[0]
                url = history[1]
                browse_data.append(time)
                browse_data.append(url)
                full_data.append(browse_data)
            storage_obj.save_csv(full_data)
            print("\n")      
            print("[+] Browser history export completed")
            print("#"*100)
            print("STAUS             : COMPLETED")
            print("EXPORTED LOCATION : "+FILE_NAME)
            print("EXPORTED TIME     : "+str(TIME))
            print("#"*100)
            print("\n") 
            confirm = input("Press Y to exit : ")
            if(confirm == "Y" or confirm == "y"):
                print("Exiting..")
        except:
            print("[-] Browser Export failed")
            confirm = input("Press Y to exit")
            if(confirm == "Y" or confirm == "y"):
                print("Exiting..")

def main():
    LABEL = '''
    
██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗░██████╗███████╗██████╗░░░░░░░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║██╔════╝██╔════╝██╔══██╗░░░░░░██║░░██║
██████╦╝██████╔╝██║░░██║░╚██╗████╗██╔╝╚█████╗░█████╗░░██████╔╝█████╗███████║
██╔══██╗██╔══██╗██║░░██║░░████╔═████║░░╚═══██╗██╔══╝░░██╔══██╗╚════╝██╔══██║
██████╦╝██║░░██║╚█████╔╝░░╚██╔╝░╚██╔╝░██████╔╝███████╗██║░░██║░░░░░░██║░░██║
╚═════╝░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░░░░╚═╝░░╚═╝
    
    
    '''
    print(LABEL)
    confirm = input("Do you want to extract browsing history (Y/N) : ")
    if(confirm == "Y" or confirm == "y"):
        DATA_OBJ = Data()
        DATA_OBJ.browsing_history()
    else:
        print("Exiting..")
        quit()

main()
