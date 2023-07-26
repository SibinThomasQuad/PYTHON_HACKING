from cProfile import label
import time
from timeit import repeat
import pyautogui
from pynput.mouse import Listener, Controller
label = """

░█████╗░██╗░░░██╗████████╗░█████╗░░░░░░░░█████╗░██╗░░░░░██╗░█████╗░██╗░░██╗
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗░░░░░░██╔══██╗██║░░░░░██║██╔══██╗██║░██╔╝
███████║██║░░░██║░░░██║░░░██║░░██║█████╗██║░░╚═╝██║░░░░░██║██║░░╚═╝█████═╝░
██╔══██║██║░░░██║░░░██║░░░██║░░██║╚════╝██║░░██╗██║░░░░░██║██║░░██╗██╔═██╗░
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝░░░░░░╚█████╔╝███████╗██║╚█████╔╝██║░╚██╗
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░░░░░░░░╚════╝░╚══════╝╚═╝░╚════╝░╚═╝░░╚═╝

"""
print(label)

CLICKS = []
class Trigger:
    def mouse_click(self,x,y):
        pyautogui.FAILSAFE = False
        pyautogui.click(x, y)

class Repeat:
    
    def trigger_clicks(self,locations):
        for location in locations:
            x = location[0]
            y = location[1]
            print("[+] clicking "+str(location))
            trigger_obj = Trigger()
            time.sleep(0.7)
            trigger_obj.mouse_click(int(x),int(y))
    
    def clicks(self,click_interval):
        print("[+] Clicks armed")
        time.sleep(click_interval)
        print("[+] clicks triggered")
        self.trigger_clicks(CLICKS)
        self.clicks(click_interval)

class Record:
    
    def on_click(self,x, y, button, pressed):
        global CLICKS
        if pressed:
            print(f"[+] Mouse clicked at X: {x}, Y: {y}")
            CLICKS.append([x,y])
            if(x == 0 and y==0):
                return False
    
    def clicks(self):
        click_interval = input("Please enter click interval in seconds > ")
        with Listener(on_click=self.on_click) as mouse_listener:
            mouse_listener.join()
        print("[+] recording stopped")
        repeat_obj = Repeat()
        repeat_obj.clicks(int(click_interval))
try:
    record_obj = Record()
    record_obj.clicks()
except:
    print("[-] ERROR OCCURED")
