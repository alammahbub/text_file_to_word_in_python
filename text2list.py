list=[]
with open('text.txt','r',encoding='utf-8') as file:
    text = file.readlines()
for line in text:
    line = line.strip('\n')
    line = line.split(' ')
    list.append(line)
    print(line)
# converted list
print(list)
# word from the list
for line in list:
    for word in line:
        print(word)
    print("    ")
