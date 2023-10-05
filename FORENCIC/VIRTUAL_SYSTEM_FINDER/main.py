import platform
import os

def check_hyper_v():
    try:
        # Check if Hyper-V is enabled on Windows
        import wmi
        c = wmi.WMI()
        for obj in c.Win32_ComputerSystem():
            if "HypervisorPresent" in obj.__dict__ and obj.HypervisorPresent:
                return "Hyper-V"
    except ImportError:
        pass
    return None

def check_dmesg():
    if platform.system() == 'Linux':
        try:
            # Check the dmesg output for common virtualization keywords
            with open('/var/log/dmesg', 'r') as dmesg_file:
                dmesg_data = dmesg_file.read()
                virtualization_indicators = ['VirtualBox', 'VMware', 'QEMU', 'Xen', 'KVM', 'Virtual Machine']
                for indicator in virtualization_indicators:
                    if indicator in dmesg_data:
                        return indicator
        except FileNotFoundError:
            pass
    return None

def check_wsl():
    if platform.system() == 'Windows':
        try:
            # Check if Windows Subsystem for Linux (WSL) is installed and running
            import subprocess
            output = subprocess.check_output(['wsl', 'echo', 'Hello from WSL'], universal_newlines=True)
            if 'Hello from WSL' in output:
                return "WSL"
        except (FileNotFoundError, subprocess.CalledProcessError):
            pass
    return None

def check_multipass():
    if platform.system() == 'Linux':
        try:
            # Check if Multipass (KVM) is installed and available
            import subprocess
            output = subprocess.check_output(['multipass', 'version'], universal_newlines=True)
            if 'multipass v' in output:
                return "Multipass (KVM)"
        except (FileNotFoundError, subprocess.CalledProcessError):
            pass
    return None

def check_vmware():
    if platform.system() == 'Linux':
        try:
            # Check if VMware Tools are installed on Linux
            import subprocess
            output = subprocess.check_output(['vmware-toolbox-cmd', '--version'], universal_newlines=True)
            if 'vmware-toolbox-cmd' in output:
                return "VMware"
        except (FileNotFoundError, subprocess.CalledProcessError):
            pass
    return None

def main():
    print("Select your operating system:")
    print("1. Windows")
    print("2. Linux")
    choice = input("Enter your choice (1/2): ")

    if choice == '1':
        hypervisor = check_hyper_v()
        wsl = check_wsl()
        if hypervisor:
            print(f"Virtualization detected: {hypervisor}")
        elif wsl:
            print(f"Virtualization detected: {wsl}")
        else:
            print("No virtualization detected on Windows.")
    elif choice == '2':
        dmesg_result = check_dmesg()
        multipass = check_multipass()
        vmware = check_vmware()
        if dmesg_result:
            print(f"Virtualization detected: {dmesg_result}")
        elif multipass:
            print(f"Virtualization detected: {multipass}")
        elif vmware:
            print(f"Virtualization detected: {vmware}")
        else:
            print("No virtualization detected on Linux.")
    else:
        print("Invalid choice. Please select 1 for Windows or 2 for Linux.")

if __name__ == "__main__":
    main()
