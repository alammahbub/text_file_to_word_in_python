k=[]
with open('text.txt','r',encoding='utf-8') as f:
    g = f.readlines()
for line in g:
    line = line.strip('\n')
    line = line.split(' ')
    k.append(line)
    print(line)
# converted list
print(k)
# word from the list
for line in k:
    for word in line:
        print(word)
    print("    ")
