from argon2 import PasswordHasher
import requests
import sys
import hashlib

password = sys.argv[1]

# Call password checker API to check the passwordin https://haveibeenpwned.com website:
def request_api_data(query_data, tail_data):
    url = 'https://api.pwnedpasswords.com/range/' + query_data
    response = requests.get(url)
    if response.status_code == 200:
        password_checker(response.text, tail_data)
    else:
        raise RuntimeError(f'Error fetching: {response.status_code}, check your password !!')

# perform the logic based on the response from https://haveibeenpwned.com website:
def password_checker(hashes, hash_to_check):
    hashed_data = (line.split(':') for line in hashes.splitlines())
    found_flag = False
    for h, count in hashed_data:
        if h == hash_to_check:
            found_flag = True
            print(f'Your password {password} has been hacked {count} times. Try some other password !!')
    if not found_flag:
        print('Ypur password is never been hacked, carry on !!')


# hash the password entered:
def pwned_api_check(paswd):
    sha1password = hashlib.sha1(paswd.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    request_api_data(first5_char, tail)


pwned_api_check(password)