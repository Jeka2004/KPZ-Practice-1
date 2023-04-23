def palindrom(text):
    word = text.split()
    palindromes = []
    for word in word:
        if word == word[::-1]:
            palindromes.append(word)
    return palindromes

text = "А роза упала на лапу Азора, тут її за кущі несуть з собою"
palindromes = palindrom(text)
print(palindromes)


import re

def validate_ip(ip_address):
    pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    if pattern.match(ip_address):
        octets = ip_address.split('.')
        for octet in octets:
            if int(octet) > 255 or int(octet) < 0:
                return False
        return True
    else:
        return False

ip_address = '192.168.0.1'
if validate_ip(ip_address):
    print(f'{ip_address} is a valid IP address.')
else:
    print(f'{ip_address} is not a valid IP address.')

import platform


def get_os():
    os_name = platform.system()

    if os_name == "Darwin":
        return "Mac"
    elif os_name == "Windows":
        return "Windows"
    elif os_name == "Linux":
        return "Linux"
    else:
        return "Unknown OS"

os_name = get_os()
print("This program is running on", os_name)


