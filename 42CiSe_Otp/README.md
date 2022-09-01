+-------------------- DESCRIPTION --------------------+

This project´s objective is to create a program that allows to register an initial key and generate a new one every time we ask for it. You can use any library that is not part of TOTP (because it would make all the dirty work).

"-g": receives a file with a 64 hexadecimal characters key at least and saves it in a file named "ft_otp.key".

"-k": receives a coded fila (ft_otp.key) and generates a temporal password, displaying it through screen.

ft_otp.key file is always encrypted.

+-------------------- FT_OTP.PY --------------------+

- Lybraries:

"qrcode_terminal" we are only using it to generate the QR code we need to show in the terminal.
"argparse˝ takes arguments as if they were from linux (command/flag) and generates them with the same name.

+-------------------- CRYPTO.PY --------------------+

- Lybraries:

The AES (advanced encryption standard) block based encryption is a standard that uses a 16 bytes string, an initialization vector IV (we make it static so it will never change) and a block. It`s CBC mode is the one used by the script. 

"getpass" prompts the user for a password without echoing. The user is prompted using the string prompt, which defaults to 'Password: ' (can be changed with getpass("yourmessage: ")).

We'll only use this program to encrypt and decrypt.

+-------------------- USEFULL COMMANDS --------------------+

- Install:

pip3 install qrcode-terminal
brew install oath-toolkit
pip3 install pycryptodome

- Optional arguments:

  python3 ft_otp.py -h, --help	      Shows a help message and exit.
  python3 ft_otp.py -g key.hex        Saves a 64 hexadecimal characters key in a file (ft_otp.key).
  python3 ft_otp.py -k ft_otp.key     Generates a temporal key using a file and shows it on screen.
  python3 ft_otp.py -qr key.hex       Shows a QR code with the secret key.

- Generates a key in a txt file (key.txt), transforms it to hex and to avoid the line break use '-c 256':

echo -n "NEVER GONNA GIVE YOU UP, NEVER GONNA LET YOU DOWN, NEVER GONNA LET YOU DOOWWN" > key.txt
xxd -c 256 -p key.txt > key.hex

But this way it'll have a line break at the end, you have to delete it.

- Shows all the info about the key:

oathtool --totp 4e6576657220676f6e61206769766520757020616e64206e6576657220676f6e61206c657420697420676f20646f776e20616c736f2e0a -v

- Refresh command oathtool every second:

watch -n 1 'oathtool --totp 4e6576657220676f6e61206769766520757020616e64206e6576657220676f6e61206c657420697420676f20646f776e20616c736f2e0a'