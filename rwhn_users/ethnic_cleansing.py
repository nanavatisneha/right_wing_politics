
all_usernames = []

for i in range(1,7):
    f = open('test%d' %i, 'r+')
    names = f.readlines()
    for n in names:
        if n not in all_usernames:
            all_usernames.append(n)
    f.close()

f = open('all_usernames','w+')
for i in all_usernames:
    f.write(i)
f.close()
