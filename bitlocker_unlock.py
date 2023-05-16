import subprocess

def unlock_bitlocker_drive(password):
    drive_letter = 'E:'  # Replace with the actual drive letter of the BitLocker-encrypted drive

    cmd = f'manage-bde -unlock {drive_letter} -password'
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate(input=password.encode())

    if process.returncode == 0:
        print(f'Successfully unlocked the BitLocker drive {drive_letter}.')
    else:
        print(f'Error unlocking the BitLocker drive {drive_letter}.')
        print(f'Error message: {error.decode()}')

# Usage example
password = 'your_bitlocker_password'
unlock_bitlocker_drive(password)
