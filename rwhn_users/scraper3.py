import os

search_names = []

fp = open('test3','r+')
names = fp.readlines()

for i in names:
     search_names.append("from%3A" + i.strip('@').strip('\n'))

for i in search_names:
    print i
    os.system('twitterscraper %s -o ./output/%s.json' %(i,i))
