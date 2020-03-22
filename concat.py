import os
import json
prefixes = input('Tien to trong ten file: ')
path = os.getcwd()
files = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path,i)) and \
         prefixes in i]
file_data = []
for file in files:
    file_data.extend(json.load(open(file,'r',encoding="utf-8")))
Filter = list(dict.fromkeys(file_data))
FilterFile = open('{}.json'.format(prefixes),'w')
FilterFile.write(json.dumps(Filter))
FilterFile.close()
input('Ghi vao file {}.json thanh cong. Nhan Enter de thoat'.format(prefixes))
