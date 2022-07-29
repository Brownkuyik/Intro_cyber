import string

words = []

class combinatons:
    def fineresult(self, record, output, n, size):
        if len(output)==5:
            words.append(output)
            print(output)
        
        if n==0:
            return
            
        i = 0
        while (i<size):
            self.fineresult(record, output  +  str(record[i]), n-1, size)
            i+=1
    

def man():
    task = combinatons()
    records = list(string.ascii_letters + string.digits)
    size = len(records)
    n = 4
    task.fineresult(records, ' ', n, size)
man()
print('lemgths is:\t', len(words))


with open("C:/Users/kuyik/Desktop/malwares/Codecamp/code.txt", 'w') as file:
    for x in words:
        file.write(f'{x} \n')