#pip install secure_delete
from secure_delete import secure_delete

secure_delete.secure_random_seed_init()
secure_delete.secure_delete('Z:\\TEST.exe')
