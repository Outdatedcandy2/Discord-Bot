from syslog import LOG_LOCAL2
from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)


file = open('key.key','wb')
file.write(key)
file.close()