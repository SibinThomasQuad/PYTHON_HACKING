from smb.SMBConnection import SMBConnection

def connect_to_smb_server(host, username, password):
    conn = SMBConnection(username, password, '', host, use_ntlm_v2=True)
    if not conn.connect(host, 139):
        return None
    return conn

def list_smb_shares(connection):
    shares = connection.listShares()
    return [share.name for share in shares if share.isDIR]

if __name__ == "__main__":
    smb_host = "192.168.3.102"
    smb_username = "Devzone"
    smb_password = "devzone"

    smb_connection = connect_to_smb_server(smb_host, smb_username, smb_password)
    if smb_connection is not None:
        print(f"Connected to SMB server at {smb_host}")
    else:
        print("Failed to connect to the SMB server.")
