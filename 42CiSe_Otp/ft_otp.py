# ************************************************************************** #
#   ft_otp.py                                                                #
#   By: maperez-                                                             #
#   Created: 2022/08/02                                                      #
# ************************************************************************** #

# Libraries

#from curses import keyname
import qrcode_terminal
import argparse
import hashlib
import struct
import hmac
import time
import re
import os
from crypto import Crypta as AES

def read_args(): # Read entry arguments.
	analyzer = init_analyzer() # Initialize args analyzer.

	return analyzer.g, analyzer.k, analyzer.qr

def init_analyzer(): # Initialyze parser.
	analyzer = argparse.ArgumentParser( # Args analyzer.
		description="Rudimentary tool to generate TOTP passwords.",
		epilog="'ft_otp' exercise from 42 Malaga Cybersecurity's Bootcamp.",
	)

	# Command options.
	analyzer.add_argument(
		"-g",
		metavar="file",
		help="Saves a 64 hexadecimal characters key in a file.",
		type=str # Whatever it takes is parsed to string.
	)
	analyzer.add_argument(
		"-k",
		metavar="file",
		help="Generates a temporal key using a file and shows it on screen.",
		type=str # Whatever it takes is parsed to string.
	)
	analyzer.add_argument(
		"-qr",
		metavar="file",
		help="Shows a QR code with the secret key.",
		type=str # Whatever it takes is parsed to string.
	)

	return analyzer.parse_args() # Obtain command args.

def validate_file(file): # Verifies that a file contains a correct key.
	global seed

	if not (os.path.isfile(file) or os.access(file, os.R_OK)): # If file doesn't exist or can't be read.
		print("Error: File doesn't exist or can't be read.")

		return False

	with open(file, "r") as f: # Extract files key.
		seed = f.read()

	if not re.match(r'^[0-9a-fA-F]{64,}$', seed): # Verifies that the key has at least 64 characters and it's in hexadecimal.
		print("Key is not hex or has less than 64 characters.")

		return False

	"""
	Explanation:
	^		   : initial str (key) limit.
	[0-9a-fA-F]: any hexadecimal character, numbers from 0 to 9, letters from a to f and from A to F.
	{64, }	   : cuantifier, indicates a minimum length (and maximum) for the hexadecimal key.
	$		   : final str (key) limit.
	"""
	
	return True

def generate_OTP(key): # Generates a temporal key (OTP) using a secret hexadecimal key.
	key_b = bytes.fromhex(key) # Encrypts the hex key in a bytes str.
	time_b = struct.pack(">Q", int(time.time() // 30)) # Codifies time in a bytes str.
	hash_b = hmac.digest(key_b, time_b, hashlib.sha1) # Generates the secret key's hash (bytes str).
	offset = hash_b[19] & 15 # Obtain offset. AND between '0b????' and '0b1111?. 
	code = struct.unpack('>I', hash_b[offset:offset + 4])[0] # 'struct.unpack' returns a list.
	code = (code & 0x7FFFFFFF) % 1000000

	"""
	Generate a HTOP value (6 digits).
	1. Generate a HMAC-SHA1 value.
		- Using the key and the current time values.
		- It'll be a 20 bytes str.
	2. Generate a 4 bytes 'str' ("Dinamic shorten").
		- Using previous HMAC-SHA1 value.
		- It'll be a 4 bytes 'str' based on 'hash[offset]' byte.
	3. Calculate HTOP value.
		- Convert 'str' to an int.
		- Apply 10^'d' module, being 'd' the amount of digits (d = 6).
	"""

	return "{:06d}".format(code) # Return 'code' as str finishing in 6 digits.

if __name__ == "__main__":
	seed_file, encrypted_file, qr = read_args() # Read command args.

	if seed_file: # If a generation of a new key is requested (-g).
		if validate_file(seed_file): # Do not use AND so it can detect errors with '-g'.
			with open("ft_otp.key", "w") as f: # Save key in a '.key' file.
				f.write(seed)

			print("Key saved in 'ft_otp.key'.")

			AES().encrypt_file("ft_otp.key") # Encrypt file with key.

			print("File 'ft_otp.key' encrypted with key.")

		else:
			exit(1) # File errors are managed in 'validate_file()'.

	elif encrypted_file or qr: # If it is needed to generate a temp code (-k) or show the keys QR (-qr).
		file = encrypted_file if encrypted_file else qr # To use the file received by one of the options (the same file but received differently). 

		if not (os.path.isfile(file) or os.access(file, os.R_OK)): # Verify that the encrypted file exists and is legible.
			print("Error: File doesn't exists or can't be read.")

			exit(1)

		else:
			seed = AES().read_file(file) # Take the files key.

			if encrypted_file: # If a key generation is needed (-k).
				print("Code generated: ", generate_OTP(seed)) # Generate and show OTP code.

			else: # If a QR code generation is needed (-qr).
				print("QR with seed: ") # Generate and show the QR.
				qrcode_terminal.draw(seed)

	else:
		print("Option not specified.")
		exit(1)
