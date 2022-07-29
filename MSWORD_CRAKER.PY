from tqdm import tqdm
from msoffcrypto import OfficeFile

path = "C:/Users/kuyik/Documents/genuine well types.docx"
wordlist = "C:/Users/kuyik/Desktop/malwares/Codecamp/code.txt"


with open(wordlist, 'r') as word:
    password_list = word.readlines()
    total_password = len(password_list)
    for word in tqdm(password_list, total=total_password, unit='word'):
        with open(path, 'rb') as file:
            off = OfficeFile(file)
            try:
                off.load_key(password=word.strip(), verify_password=True)
            except Exception as e:
                print('next...', e)
                continue
            else:
                print('\npassword found as: ', word)
                break

