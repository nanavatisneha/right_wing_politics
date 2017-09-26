import json
import csv
import sys

search_names = []
names = []
count = 0

fp = open('all_usernames','r+')
names = fp.readlines()
fp.close()

for i in names:
     search_names.append("from%3A" + i.strip('@').strip('\n'))

for i in search_names:
    fp_j = open('./output/%s.json' % i, 'r+')
    x = json.loads(fp_j.read())
    wr = open("./csv_files/%s.csv" %i, "w+")
    fp_c = csv.writer(wr)
    fp_c.writerow(["timestamp", "user", "fullname", "text", "retweets", "replies", "likes"])
    for x in x:
        fp_c.writerow([x["timestamp"].encode('utf-8'), x["user"].encode('utf-8'), x["fullname"].encode('utf-8'), x["text"].encode('utf-8'), x["retweets"].encode('utf-8'), x["replies"].encode('utf-8'), x["likes"].encode('utf-8')])
    sys.stdout.write("\r done with %d files" %count)
    sys.stdout.flush()
    count = count+1
    fp_j.close()
    wr.close()
