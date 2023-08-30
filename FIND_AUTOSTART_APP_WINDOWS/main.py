import winreg

def get_startup_programs():
    startup_programs = []
    
    # Iterate through user profiles
    key = winreg.HKEY_USERS
    try:
        hkey = winreg.OpenKey(key, None)
        index = 0
        while True:
            try:
                user_sid = winreg.EnumKey(hkey, index)
                subkey = fr"{user_sid}\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
                try:
                    user_hkey = winreg.OpenKey(key, subkey)
                    subindex = 0
                    while True:
                        try:
                            name, value, _ = winreg.EnumValue(user_hkey, subindex)
                            startup_programs.append((name, value, user_sid))
                            subindex += 1
                        except OSError:
                            break
                    winreg.CloseKey(user_hkey)
                except Exception as e:
                    pass
                index += 1
            except OSError:
                break
        winreg.CloseKey(hkey)
    except Exception as e:
        print("An error occurred:", e)

    return startup_programs

def main():
    startup_programs = get_startup_programs()
    if startup_programs:
        print("List of auto-starting executable files:")
        for name, value, user_sid in startup_programs:
            print(f"User: {user_sid}, Name: {name}, Value: {value}")
    else:
        print("No auto-starting executable files found.")

if __name__ == "__main__":
    main()
