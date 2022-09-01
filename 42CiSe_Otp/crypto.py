# ************************************************************************** #
#   crypto.py                                                                #
#   By: maperez-                                                             #
#   Created: 2022/08/02                                                      #
# ************************************************************************** #

# Libraries
from getpass import getpass
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

class Crypta: # Basic encrypt/disencrypt implementationusing AES in CBC mode.
	key = None # Necesary data.
	IV = None
	mode = AES.MODE_CBC
	block = None

	def __init__(self): # Class builder.
		self.IV = "cb71De88D9ab1640".encode("utf-8")
		self.block = 16 # Block size: 128 bits.

	"""
	The AES encode in CBC mode requires: a key (password), an initialization vector (seed) and a block size, all of them 16 bytes long.
	For this subject, IV will be a constant between instances, only asking for a password to the user to access to files content.
	"""

	def encrypt(self, clear_text): # Encodes a text using AES in CBC mode with initialization vector IV.
		self.key = getpass("Insert password: ").encode("utf-8")

		if len(self.key) != 16: # Validate keys length.
			print("Key must be 16 bytes long.")
			exit(1)

		cipher = AES.new(self.key, self.mode, self.IV) # Encode procedure.

		return cipher.encrypt(pad(clear_text.encode("utf-8"), self.block)) # Returns messages encoded being a multiple of the blocks size (16 bytes).

	def decrypt(self, hidden_text): # Decrypts text using AES in CBC mode with a IV starting vector.
		self.key = getpass("Insert password: ").encode("utf-8")
		
		if len(self.key) != 16:
			print("Key must have 16 characters at least.")
			exit(1)
		
		try:
			decrypter = AES.new(self.key, self.mode, self.IV) # Decryption method.
		
			return unpad(decrypter.decrypt(hidden_text), self.block).decode("utf-8", "ignore") # Decrypt, remove padding and recover str.
																		
		except:
			print("Incorrect password.")
			exit(1)
      
	def encrypt_file(self, file): # Encrypts a file using AES in CBC mode with a IV starting vector.
		with open(file, "r") as f: # Read files content.
			content = f.read()
		
		hidden = self.encrypt(content) # Encrypt files content.
		
		with open(file, "wb") as f: # Write content (encrypted) in file (bytes).
			f.write(hidden)
		
		return hidden
	
	def decrypt_file(self, file): # Decrypts a file using AES in CBC mode with a IV starting vector.
		with open(file, "rb") as f: # Read files content (bytes).
			content = f.read()
		
		clear = self.decrypt(content) # Decrypt files content.
		
		with open(file, "w") as f: # Write content (decrypted) in file.
			f.write(clear)
		
		return clear
	
	def read_file(self, file): # Reads a encrypted file content.
		with open(file, "rb") as f: # Read content.
			content = f.read()
		
		clear = self.decrypt(content) # Decrypt content.
		
		return clear
