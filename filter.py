file = open('id.txt','r')
List = file.readlines()
for x in List:
    open('id2.txt','a').write(x)