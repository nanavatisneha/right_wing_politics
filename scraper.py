fp = open('usernames','r+')
names = fp.readlines()

search_names = []

for i in names:
     search_names.append("from%3A" + i.strip('@').strip('\n'))
