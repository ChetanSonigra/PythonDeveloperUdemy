import shutil, os, re, datetime, time

shutil.unpack_archive('Project+Day+9.zip', 'python1/Day9/project_day9', 'zip')

begin = time.time()

p = os.walk('python1/Day9/project_day9/My_Big_Directory')
d = dict()

for folder, subfolder, files in p:
    for file in files:
        with open(f'{folder}/{file}', 'r') as f:
            s_file = f.read()
            res = re.search(r'N\D{3}-\d{5}', s_file)
            if res:
                d[file.title()]= s_file[res.start(): res.end()]

today = datetime.datetime.today().strftime('%d/%m/%y')
print('-'*30)
print(f'Search date: [{today}]\n')
print('FILE', " "*10, 'SERIAL NO.')
print('_'*4, ' '*10,'_'*10)

for key, value in d.items():
    temp = 16-len(key)
    print(key, value, sep=' '*temp)
print(f'\nNumbers found: {len(d)}')  
end = time.time()
t = end - begin
t = round(t)
print(f'Search duration: {t} seconds')  
print('_'*30)
