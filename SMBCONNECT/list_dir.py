from smb.SMBConnection import SMBConnection

def list_smb_directories(host, username, password, share_name):
    try:
        conn = SMBConnection(username, password, '', host, use_ntlm_v2=True)
        conn.connect(host, 139)
        directories = conn.listPath(share_name, '/')
        conn.close()
        return [entry.filename for entry in directories if entry.isDirectory]
    except Exception as e:
        print(f"Error: {e}")
    return []

if __name__ == "__main__":
    smb_host = "192.168.3.102"
    smb_username = "Devzone"
    smb_password = "devzone"
    smb_share = "Devzone"

    directories = list_smb_directories(smb_host, smb_username, smb_password, smb_share)
    if directories:
        print(f"Directories in '{smb_share}' share:")
        for directory in directories:
            print(directory)
    else:
        print(f"No directories found in '{smb_share}' share.")

