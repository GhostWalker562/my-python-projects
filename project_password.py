import re



def main():
    print("Type a password:")
    # Colon into variable type
    # Followed by initilization which ask for input
    password : str = input()
    check_pass(password)


def check_pass(Password:str):
    # Regex,
	if re.match(r'[a-zA-Z0-9]{4,}', Password) is not None:
		print ('Strong Password')
	else:
		print ('Weak Password')
        
# Defines the main function for the file.
if __name__ == "__main__":
    main()