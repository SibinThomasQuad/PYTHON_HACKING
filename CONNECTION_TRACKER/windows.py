import psutil

def list_connections():
    print("{:<20} {:<20} {:<10} {:<10} {:<10} {}".format(
        "Local Address", "Local Port", "Remote Address", "Remote Port", "Status", "Application"
    ))

    for conn in psutil.net_connections(kind='inet'):
        local_addr = conn.laddr.ip
        local_port = conn.laddr.port
        remote_addr = conn.raddr.ip if conn.raddr else "-"
        remote_port = conn.raddr.port if conn.raddr else "-"
        status = conn.status
        pid = conn.pid or "-"
        
        try:
            app_name = psutil.Process(conn.pid).name()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            app_name = "-"

        print("{:<20} {:<20} {:<20} {:<20} {:<10} {}".format(
            local_addr, local_port, remote_addr, remote_port, status, app_name
        ))

if __name__ == '__main__':
    list_connections()
