# digital-politics
Dataset for Rightwing Hindu Nationalists Tweets. #BlessedToBeFollowed by Modi

This is a commentary regarding the data. Plan is to explain all the pointers in the data. 
The data is shared in this GDrive folder and can be accessed by opening it in MS Excel or Google Sheets.
Each user has its own excel sheets and the details available are: username, full name, timestamp of the tweet, content, no. of retweets, no. of likes, no. of replies.
The original format of the data is stored in .json file. This is not user-friendly and thus I made a converter to use the .csv format. 

How to get tweet data from each user
First, the user name of the twitter user is taken and then a “from%3A” is appended in from of the username after removing @ sign. This is then passed through a Twitter Scraper code (all the codes are zipped and will be uploaded in the same folder). 
Then the data from each account is scraped with the necessary fields (defined before) and stored in a new file in format “from%3A+username”.json. This file is converted to .csv and accessed.

What to do next?
The idea is to use Topic Modelling on the data we have. Brief intro about topic modelling and the model I am using can be found here.
We have data from around 139 accounts. I am also scraping data from media houses in and outside India, around 56 accounts.
Link to media houses: https://airtable.com/invite/l?inviteId=invnGzEGByYU6jekp&inviteToken=7384807d30aac3759ff415348eef1305
Link to twitter users: https://airtable.com/invite/l?inviteId=invunaTAc077sK8jF&inviteToken=19c4b94e19ef564d6a78f62001b4f0ce
The reason for this is we can perform topic modelling on them and identify the topics that are being discussed by the media houses and compare it against the topics being discussed by the hindu nationalist handles.
So open question is: do we want to do a topic modelling (identifying the topic of discussion through their mention in text/data against a time frame, or over all and compare the output of the algorithm with topics zeroed by us physical).
Let’s discuss this!



