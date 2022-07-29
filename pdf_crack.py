import pikepdf

password_file = 'C:/Users/kuyik/Desktop/malwares/Codecamp/password.txt'
lock_file = "C:/Users/kuyik/Documents/400L¹ Past-Questions.pdf"

with open(password_file) as passcode:
    password_list = passcode.readlines()
    total_pass = len(password_list)

    for index,passwords in enumerate(password_list):
        try:
            with pikepdf.open(lock_file, password = passwords.strip()) as pdf_file:
                print('\nPassword seen'.center(40,'='))
                print('file open\nPassword is: ', passwords)
                break
        except:
            print('\n')
            print('trying password', passwords, 'fails')
            scanning = (index/total_pass)*100
            print('scannig password complete: ', round(scanning, 2))
            continue

