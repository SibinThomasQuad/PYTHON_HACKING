import nmap

def host_discovery(target):
    """
    Perform host discovery using Nmap.

    Args:
    - target (str): Target IP address or hostname.

    Returns:
    - list: List of discovered hosts that are up.
    """
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-sn')
    
    hosts = [host for host in nm.all_hosts() if nm[host].state() == 'up']
    return hosts

def service_version_detection(target):
    """
    Perform service version detection using Nmap.

    Args:
    - target (str): Target IP address or hostname.

    Returns:
    - dict: Dictionary containing service version information for open ports.
    """
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-sV')
    
    results = {}
    for host in nm.all_hosts():
        results[host] = {}
        for port in nm[host]['tcp']:
            service_info = nm[host]['tcp'][port]
            results[host][port] = service_info['name'], service_info['product'], service_info['version']

    return results

def os_fingerprinting(target):
    """
    Perform OS fingerprinting using Nmap.

    Args:
    - target (str): Target IP address or hostname.

    Returns:
    - dict: Dictionary containing detected OS information for each host.
    """
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-O')
    
    results = {}
    for host in nm.all_hosts():
        os_info = nm[host]['osmatch']
        results[host] = [os['name'] for os in os_info]

    return results

def script_scan(target):
    """
    Perform script scanning using Nmap.

    Args:
    - target (str): Target IP address or hostname.

    Returns:
    - dict: Dictionary containing the output of Nmap scripts for each host.
    """
    nm = nmap.PortScanner()
    nm.scan(target, arguments='--script=default')
    
    results = {}
    for host in nm.all_hosts():
        scripts_output = nm[host]['scripts']
        results[host] = scripts_output

    return results

def traceroute(target):
    """
    Perform traceroute using Nmap.

    Args:
    - target (str): Target IP address or hostname.

    Returns:
    - dict: Dictionary containing hop information for each host.
    """
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-traceroute')
    
    results = {}
    for host in nm.all_hosts():
        hops = nm[host]['osmatch'][0]['osclass'][0]['cpe']
        results[host] = hops

    return results

def aggressive_scan(target):
    """
    Perform aggressive scan using Nmap.

    Args:
    - target (str): Target IP address or hostname.

    Returns:
    - dict: Dictionary containing open port information from an aggressive scan.
    """
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-A')
    
    results = {}
    for host in nm.all_hosts():
        service_info = nm[host]['tcp']
        results[host] = {port: {'name': service_info[port]['name'], 'state': service_info[port]['state']} for port in service_info}

    return results

def banner_grabbing(target, ports=None):
    """
    Perform banner grabbing using Nmap.

    Args:
    - target (str): Target IP address or hostname.
    - ports (list): List of ports to grab banners from. If None, all open ports are considered.

    Returns:
    - dict: Dictionary containing banners for specified ports or all open ports.
    """
    nm = nmap.PortScanner()
    
    if ports:
        port_str = ','.join(map(str, ports))
        nm.scan(target, arguments=f'-p {port_str} --script=banner')
    else:
        nm.scan(target, arguments='--script=banner')

    results = {}
    for host in nm.all_hosts():
        banners = nm[host]['tcp']
        results[host] = {port: banners[port]['script'] for port in banners}

    return results

def ping_scan(target):
    """
    Perform ping scanning using Nmap.

    Args:
    - target (str): Target IP address or hostname.

    Returns:
    - dict: Dictionary containing ping scan results for each host.
    """
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-sn')
    
    results = {}
    for host in nm.all_hosts():
        results[host] = nm[host]['status']['state']

    return results

def version_intensity_scan(target):
    """
    Perform version intensity scanning using Nmap.

    Args:
    - target (str): Target IP address or hostname.

    Returns:
    - dict: Dictionary containing version intensity scan results for each host.
    """
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-sV --version-intensity 9')
    
    results = {}
    for host in nm.all_hosts():
        results[host] = nm[host]['osmatch'][0]['osclass'][0]['cpe']

    return results

# Example Usage
target_host = '127.0.0.1'

print("Host Discovery:")
print(host_discovery(target_host))

print("\nService Version Detection:")
print(service_version_detection(target_host))

print("\nOS Fingerprinting:")
print(os_fingerprinting(target_host))

print("\nScript Scan:")
print(script_scan(target_host))

print("\nTraceroute:")
print(traceroute(target_host))

print("\nAggressive Scan:")
print(aggressive_scan(target_host))

print("\nBanner Grabbing:")
print(banner_grabbing(target_host))

print("\nPing Scan:")
print(ping_scan(target_host))

print("\nVersion Intensity Scan:")
print(version_intensity_scan(target_host))
